def palindromes_of_specific_lengths(s):

    def is_letter_palindrome(substr):
        return substr.isalpha() and substr == substr[::-1]
    result = set()
    substring = s[29:97].lower()
    for length in range(12, 19):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_letter_palindrome(candidate):
                result.add(candidate)
    return result