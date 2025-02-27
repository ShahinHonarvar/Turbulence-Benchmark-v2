def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    n = len(s)
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for length in range(7, n + 1):
        for i in range(n - length + 1):
            substr = s[i:i + length]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes