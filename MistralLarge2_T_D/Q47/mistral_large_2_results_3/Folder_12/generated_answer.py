def palindromes_of_specific_lengths(s):

    def is_palindrome(p):
        return p == p[::-1]
    substr = s[62:89].lower()
    palindromes = set()
    for length in range(18, 22):
        for i in range(len(substr) - length + 1):
            substring = substr[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes