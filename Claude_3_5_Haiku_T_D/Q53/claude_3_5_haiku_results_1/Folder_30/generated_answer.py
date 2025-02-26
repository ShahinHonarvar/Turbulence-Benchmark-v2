def palindrome_of_length_at_least_n(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def is_only_letters(substring):
        return substring.isalpha()
    palindromes = set()
    s = s.lower()
    n = 16
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if len(substring) >= n and is_palindrome(substring) and is_only_letters(substring):
                palindromes.add(substring)
    return palindromes