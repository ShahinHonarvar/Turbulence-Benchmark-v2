def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 97, n + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes