def palindrome_of_length_at_least_n(s):

    def is_valid_palindrome(substring):
        return substring.isalpha() and substring == substring[::-1]
    palindromes = set()
    s = s.lower()
    n = 10
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if is_valid_palindrome(substring):
                palindromes.add(substring)
    return palindromes