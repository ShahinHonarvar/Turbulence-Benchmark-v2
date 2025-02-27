def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        sub = ''.join(filter(str.isalpha, sub)).lower()
        return sub == sub[::-1]
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 88
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            substring = s[i:j]
            if len(substring) >= n and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes