def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = len(s)
    for start in range(n):
        for end in range(start + 35, n + 1):
            substr = s[start:end]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes