def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    palindromes = set()
    substring = s[33:86]
    for length in range(26, 32):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes