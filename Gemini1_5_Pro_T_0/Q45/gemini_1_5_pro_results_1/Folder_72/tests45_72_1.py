from Q45.gemini_1_5_pro_results_1.Folder_72.generated_answer import palindromes_between_indices


def test_string_of_similar_chars():
    s = ''.join('a' for _ in range(7 + 1))
    if 7 - 1 + 1 < 6:
        assert not palindromes_between_indices(s)
    else:
        assert palindromes_between_indices(s) == {'a' * i for i in range(6, 7 - 1 + 2)}


def test_string_of_distinct_chars():
    s = 'abcdefghijkl'
    assert not palindromes_between_indices(s)


def test_string_of_spaces():
    s = ' ' * (7 * 2)
    assert not palindromes_between_indices(s)


def test_string_of_same_punctuations():
    s = '@' * (7 * 2)
    assert not palindromes_between_indices(s)


def test_string_of_same_numbers():
    s = '0' * (7 * 2)
    assert not palindromes_between_indices(s)
        

def test_length_of_palindrome():
    s = ''.join('a' for _ in range(7 + 1))
    returned_result = palindromes_between_indices(s)
    for i in returned_result:
        assert 6 <= len(i) <= 7 - 1 + 1


def test_string_of_spaces_and_letters():
    s = ' a ' * (7 + 1)
    ss = s[1:7 + 1]
    ss = ss.replace(' ', '')
    length = len(ss)
    if length < 6:
        assert not palindromes_between_indices(s)
    else:
        min_ = min(length, 6)
        max_ = max(length, 6)
        assert palindromes_between_indices(s) == {'a' * i for i in range(min_, max_ + 1)}


def test_string_of_punctuations_and_letters():
    s = '%a&' * (7 + 1)
    ss = s[1:7 + 1]
    ss = ss.replace('%', '')
    ss = ss.replace('&', '')
    length = len(ss)
    if length < 6:
        assert not palindromes_between_indices(s)
    else:
        min_ = min(length, 6)
        max_ = max(length, 6)
        assert palindromes_between_indices(s) == {'a' * i for i in range(min_, max_ + 1)}
        