from Q47.mistral_large_2_results_3.Folder_58.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(283, 126)
    m = min(283 - 125 + 1, 126)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(109, m + 1)}


def test_string_of_similar_nums():
    n = max(283, 126)
    m = min(283 - 125 - 1, 126)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (283 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (283 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (283 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(283 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 109 <= len(i) <= 126


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(283 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[125: 283 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (283 * 3)
    assert not palindromes_of_specific_lengths(s)
    