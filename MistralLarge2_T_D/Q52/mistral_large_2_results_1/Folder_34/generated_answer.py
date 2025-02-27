def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    palindromes = set()
    length = 33
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring.lower())
    return palindromes