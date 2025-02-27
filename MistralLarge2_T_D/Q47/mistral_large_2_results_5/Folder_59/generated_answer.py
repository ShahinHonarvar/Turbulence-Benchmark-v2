def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    substr = s[:101]
    palindromes = set()
    for length in range(3, 16):
        for i in range(len(substr) - length + 1):
            substring = substr[i:i + length]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring.lower())
    return palindromes