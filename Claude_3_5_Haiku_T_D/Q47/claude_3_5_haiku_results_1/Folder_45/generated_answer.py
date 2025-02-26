def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_alpha_only(substring):
        return substring.isalpha()
    palindromes = set()
    if len(s) <= 140:
        return palindromes
    substring = s[70:141]
    for length in range(3, 61):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_alpha_only(candidate):
                palindromes.add(candidate.lower())
    return palindromes