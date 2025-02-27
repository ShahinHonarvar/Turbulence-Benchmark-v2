def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    substring = s[44:100].lower()
    palindromes = set()
    for length in range(13, 43):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes