from Q37.deepseek_coder_results_5.Folder_35.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (403 + 2)
    if '(' <= 'm' <= ']':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(403 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[155:403+1]
    for char in sliced_s:
        if '(' <= char <= ']':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(403*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('('), ord(']') + 1))
    for _ in range(403 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('('), ord(']') + 1))
    for _ in range(155 + 1):
        s += '('
    for _ in range(403 - 155):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
