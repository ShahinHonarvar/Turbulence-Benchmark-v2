def palindromes_of_specific_lengths(string):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]

    def is_letter_only(s):
        return s.isalpha()
    result = set()
    substring = string[35:89]
    for length in range(24, 34):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_letter_only(candidate):
                result.add(candidate.lower())
    return result