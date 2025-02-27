def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    substring = s[17:96]
    palindromes = set()
    for length in range(13, 50):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                palindromes.add(candidate)
    return palindromes