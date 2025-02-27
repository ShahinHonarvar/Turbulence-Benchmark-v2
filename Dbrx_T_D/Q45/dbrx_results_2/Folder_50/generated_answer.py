from functools import reduce
    import string

def palindromes_between_indices(s):
    valid_chars = set(string.ascii_letters)
    chars_in_range = reduce(lambda x, y: x + y, [list(s[i]) for i in range(4, 9) if s[i] in valid_chars])
    palindromes = set()
    for idx, char in enumerate(chars_in_range):
        for length in range(5, len(chars_in_range) - idx + 1):
            if chars_in_range[idx:idx + length] == chars_in_range[idx:idx + length][::-1]:
                palindromes.add(''.join(chars_in_range[idx:idx + length]))
    return palindromes