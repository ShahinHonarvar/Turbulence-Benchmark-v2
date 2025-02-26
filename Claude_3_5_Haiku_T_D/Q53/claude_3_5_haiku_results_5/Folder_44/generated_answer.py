def palindrome_of_length_at_least_n(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def is_only_letters(substring):
        return substring.isalpha()
    palindromes = set()
    s = s.lower()
    n = 89
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if is_only_letters(substring) and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes