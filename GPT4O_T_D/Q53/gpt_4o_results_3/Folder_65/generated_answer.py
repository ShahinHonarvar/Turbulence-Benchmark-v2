def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    palindromes = set()

    def is_palindrome(substring):
        return substring == substring[::-1]
    for i in range(n):
        for j in range(i + 15, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes