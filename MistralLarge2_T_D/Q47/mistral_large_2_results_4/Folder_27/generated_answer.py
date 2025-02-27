def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    palindromes = set()
    for length in range(26, 30):
        for i in range(13, 100 - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes