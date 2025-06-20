from Q36.command_results_5.Folder_12.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (84 + 2)
    if 'm' < 'm' < 'w':
        assert not filter_chars(s)
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(84 * 2))
    sliced_s = set(s[32 + 1:84])
    c = 0
    for char in sliced_s:
        if 'm' < char < 'w':
            c += s.count(char)

    assert len(filter_chars(s)) == len(s) - c


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(84*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    given_range = list(range(ord('m') + 1, ord('w')))
    s = ''
    for _ in range(84 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ' + string.digits)
        while ord(char) in given_range:
            char = random.choice(string.ascii_letters + '$ % & * + < = > @ ' + string.digits)
        s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    for _ in range(84 + 10):
        char = random.randint(ord('m') + 1, ord('w')-1)
        s += chr(char)

    sliced_s = s[32 + 1:84]
    result = filter_chars(s)
    for char in sliced_s:
        assert char not in result
