from Q47.command_r_plus_results_4.Folder_15.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(6, 6)
    m = min(6 - 0 + 1, 6)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(3, m + 1)}


def test_string_of_similar_nums():
    n = max(6, 6)
    m = min(6 - 0 - 1, 6)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (6 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (6 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (6 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(6 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 3 <= len(i) <= 6


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(6 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[0: 6 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (6 * 3)
    assert not palindromes_of_specific_lengths(s)
    