def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    palindromes = set()
    substr = s[36:93].lower()
    for length in range(10, 36):
        for i in range(len(substr) - length + 1):
            substring = substr[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes