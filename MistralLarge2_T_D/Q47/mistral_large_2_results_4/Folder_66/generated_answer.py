def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    substr = s[32:80].lower()
    palindromes = set()
    for length in range(35, 42):
        for i in range(len(substr) - length + 1):
            substring = substr[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes