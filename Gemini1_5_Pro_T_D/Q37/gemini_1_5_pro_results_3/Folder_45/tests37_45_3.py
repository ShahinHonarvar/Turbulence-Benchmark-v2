from Q37.gemini_1_5_pro_results_3.Folder_45.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (94 + 2)
    if '.' <= 'm' <= 'b':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(94 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[72:94+1]
    for char in sliced_s:
        if '.' <= char <= 'b':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(94*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('.'), ord('b') + 1))
    for _ in range(94 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('.'), ord('b') + 1))
    for _ in range(72 + 1):
        s += '.'
    for _ in range(94 - 72):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
