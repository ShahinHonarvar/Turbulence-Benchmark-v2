from Q37.Llama_3_70_results_3.Folder_57.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (85 + 2)
    if '!' <= 'm' <= 'B':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(85 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[27:85+1]
    for char in sliced_s:
        if '!' <= char <= 'B':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(85*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('!'), ord('B') + 1))
    for _ in range(85 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('!'), ord('B') + 1))
    for _ in range(27 + 1):
        s += '!'
    for _ in range(85 - 27):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
