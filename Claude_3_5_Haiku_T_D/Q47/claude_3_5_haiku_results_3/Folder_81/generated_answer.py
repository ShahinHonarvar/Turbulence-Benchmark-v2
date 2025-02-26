def palindromes_of_specific_lengths(string):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1] and s.isalpha()
    result = set()
    if len(string) < 123:
        return result
    substring = string[12:123]
    for length in range(12, 221):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate):
                result.add(candidate)
    return result