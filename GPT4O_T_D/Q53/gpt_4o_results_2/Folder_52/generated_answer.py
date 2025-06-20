def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for start in range(n):
        for end in range(start + 14, n + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes