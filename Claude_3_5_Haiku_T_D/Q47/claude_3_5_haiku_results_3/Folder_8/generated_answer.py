def palindromes_of_specific_lengths(s):

    def is_letter_palindrome(substr):
        return substr.isalpha() and substr == substr[::-1]
    result = set()
    substring = s[17:73]
    for start in range(len(substring)):
        for length in (50, 51):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if is_letter_palindrome(candidate.lower()):
                result.add(candidate)
    return result