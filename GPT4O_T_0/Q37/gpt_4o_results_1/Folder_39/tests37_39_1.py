from Q37.gpt_4o_results_1.Folder_39.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (81 + 2)
    if 'A' <= 'm' <= 'U':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(81 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[52:81+1]
    for char in sliced_s:
        if 'A' <= char <= 'U':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(81*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('A'), ord('U') + 1))
    for _ in range(81 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('A'), ord('U') + 1))
    for _ in range(52 + 1):
        s += 'A'
    for _ in range(81 - 52):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
