from Q37.gemma_2_27_results_5.Folder_31.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (96 + 2)
    if '<' <= 'm' <= 'w':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(96 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[57:96+1]
    for char in sliced_s:
        if '<' <= char <= 'w':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(96*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('<'), ord('w') + 1))
    for _ in range(96 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('<'), ord('w') + 1))
    for _ in range(57 + 1):
        s += '<'
    for _ in range(96 - 57):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
