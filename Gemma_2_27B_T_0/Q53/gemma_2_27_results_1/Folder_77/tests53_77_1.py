from Q53.gemma_2_27_results_1.Folder_77.generated_answer import palindrome_of_length_at_least_n
import string
import random


def test_string_of_similar_chars_of_length_149():
    s = ''.join('a' for _ in range(149))
    assert palindrome_of_length_at_least_n(s) == {s}


def test_string_of_similar_chars_of_length_greater_than_149():
    ss = ''.join('a' for _ in range(149 * 2))
    s = ss[:149]
    result = []
    for i in range(0, 149 + 1):
        result.append(s + ('a' * i))
    assert palindrome_of_length_at_least_n(ss) == set(result)


def test_string_of_many_chars():
    s = 'abcdef'
    r = ''
    for _ in range(149):
        r += s
    assert not palindrome_of_length_at_least_n(r)


def test_string_of_spaces():
    s = ' ' * (149 * 2)
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_spaces_and_letters():
    s = ' a ' * 149 * 2
    ss = s.replace(' ','')
    sss = ss[:149]
    result = []
    for i in range(0, 149 + 1):
        result.append(sss + ('a' * i))
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_punctuations():
    s = ''.join(random.choice(string.punctuation) for _ in range(149))
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_punctuations_and_letters():
    s = 'a%' * 149
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_many_punctuations_and_letters():
    s = 'a%' * 149 * 2
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_many_punctuations_and_letters_and_spaces():
    s = 'a% ' * 149 * 2
    assert not palindrome_of_length_at_least_n(s)


def test_length_of_palindrome():
    n = random.randint(5,10)
    s = 'a' * (149 * n)
    returned_result = palindrome_of_length_at_least_n(s)
    for i in returned_result:
        assert 149 <= len(i)


def test_string_of_similar_nums():
    s = ''.join('0' for _ in range(149))
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_many_similar_nums():
    ss = ''.join('0' for _ in range(149 * 2))
    s = ss[:149]
    result = []
    for i in range(0, 149 + 1):
        result.append(s + ('0' * i))
    assert not palindrome_of_length_at_least_n(ss)


def test_numeric_string():
    s = ''.join(random.choice(string.digits) for _ in range(149 // 2))
    if 149 % 2 == 0:
        s += s[::-1]
    else:
        s += (random.choice(string.digits) + s[::-1])
    assert not palindrome_of_length_at_least_n(s)
    