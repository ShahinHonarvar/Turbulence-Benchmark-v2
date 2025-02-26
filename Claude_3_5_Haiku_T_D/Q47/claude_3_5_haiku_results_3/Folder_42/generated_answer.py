def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_alpha_only(substr):
        return substr.isalpha()
    palindromes = set()
    substring = s[43:96]
    for length in range(18, 48):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_alpha_only(candidate):
                palindromes.add(candidate)
    return palindromes