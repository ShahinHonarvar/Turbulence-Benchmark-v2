from Q37.claude_3_5_haiku_results_4.Folder_96.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (92 + 2)
    if '!' <= 'm' <= 's':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(92 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[86:92+1]
    for char in sliced_s:
        if '!' <= char <= 's':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(92*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('!'), ord('s') + 1))
    for _ in range(92 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('!'), ord('s') + 1))
    for _ in range(86 + 1):
        s += '!'
    for _ in range(92 - 86):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
