from Q36.gpt_4o_results_4.Folder_100.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (69 + 2)
    if 'B' < 'm' < 'r':
        assert not filter_chars(s)
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(69 * 2))
    sliced_s = set(s[43 + 1:69])
    c = 0
    for char in sliced_s:
        if 'B' < char < 'r':
            c += s.count(char)

    assert len(filter_chars(s)) == len(s) - c


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(69*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    given_range = list(range(ord('B') + 1, ord('r')))
    s = ''
    for _ in range(69 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ' + string.digits)
        while ord(char) in given_range:
            char = random.choice(string.ascii_letters + '$ % & * + < = > @ ' + string.digits)
        s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    for _ in range(69 + 10):
        char = random.randint(ord('B') + 1, ord('r')-1)
        s += chr(char)

    sliced_s = s[43 + 1:69]
    result = filter_chars(s)
    for char in sliced_s:
        assert char not in result
