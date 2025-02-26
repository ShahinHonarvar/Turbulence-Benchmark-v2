def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def is_alpha_string(substr):
        return all((char.isalpha() for char in substr))
    if len(s) < 85:
        return set()
    substring = s[24:85].lower()
    result_set = set()
    for length in range(21, 32):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_alpha_string(candidate):
                result_set.add(candidate)
    return result_set