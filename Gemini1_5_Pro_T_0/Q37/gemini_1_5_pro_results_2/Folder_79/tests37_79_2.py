from Q37.gemini_1_5_pro_results_2.Folder_79.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (52 + 2)
    if '@' <= 'm' <= 'T':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(52 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[10:52+1]
    for char in sliced_s:
        if '@' <= char <= 'T':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(52*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('@'), ord('T') + 1))
    for _ in range(52 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('@'), ord('T') + 1))
    for _ in range(10 + 1):
        s += '@'
    for _ in range(52 - 10):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
