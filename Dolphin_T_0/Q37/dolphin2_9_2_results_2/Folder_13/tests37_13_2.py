from Q37.dolphin2_9_2_results_2.Folder_13.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (854 + 2)
    if '9' <= 'm' <= 's':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(854 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[124:854+1]
    for char in sliced_s:
        if '9' <= char <= 's':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(854*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('9'), ord('s') + 1))
    for _ in range(854 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('9'), ord('s') + 1))
    for _ in range(124 + 1):
        s += '9'
    for _ in range(854 - 124):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
