from Q47.mistral_large_2_results_2.Folder_90.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(280, 151)
    m = min(280 - 106 + 1, 151)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(136, m + 1)}


def test_string_of_similar_nums():
    n = max(280, 151)
    m = min(280 - 106 - 1, 151)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (280 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (280 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (280 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(280 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 136 <= len(i) <= 151


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(280 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[106: 280 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (280 * 3)
    assert not palindromes_of_specific_lengths(s)
    