def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_alphabetic(substring):
        return substring.isalpha()
    result = set()
    substring = s[17:96]
    for length in range(13, 50):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_alphabetic(candidate):
                result.add(candidate.lower())
    return result