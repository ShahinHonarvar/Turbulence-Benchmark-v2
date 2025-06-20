from Q47.codegemma_results_2.Folder_100.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(96, 18)
    m = min(96 - 29 + 1, 18)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(12, m + 1)}


def test_string_of_similar_nums():
    n = max(96, 18)
    m = min(96 - 29 - 1, 18)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (96 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (96 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (96 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(96 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 12 <= len(i) <= 18


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(96 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[29: 96 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (96 * 3)
    assert not palindromes_of_specific_lengths(s)
    