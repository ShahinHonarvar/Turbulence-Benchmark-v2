from Q47.mistral_large_2_results_3.Folder_32.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(77, 47)
    m = min(77 - 16 + 1, 47)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(43, m + 1)}


def test_string_of_similar_nums():
    n = max(77, 47)
    m = min(77 - 16 - 1, 47)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (77 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (77 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (77 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(77 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 43 <= len(i) <= 47


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(77 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[16: 77 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (77 * 3)
    assert not palindromes_of_specific_lengths(s)
    