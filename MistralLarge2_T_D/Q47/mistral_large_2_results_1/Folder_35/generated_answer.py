def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    substring = s[34:91].lower()
    palindromes = set()
    for length in range(14, 40):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes