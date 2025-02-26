def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_alpha_only(substr):
        return substr.isalpha()
    palindromes = set()
    if len(s) < 72:
        return palindromes
    substring = s[32:72]
    for length in range(21, 33):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate) and is_alpha_only(candidate):
                palindromes.add(candidate.lower())
    return palindromes