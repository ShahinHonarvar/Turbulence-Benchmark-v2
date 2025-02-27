def palindromes_of_specific_lengths(string):

    def is_palindrome(s):
        return s == s[::-1]
    substr = string[:21].lower()
    palindromes = set()
    for length in range(5, 81):
        for i in range(21 - length + 1):
            substring = substr[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes