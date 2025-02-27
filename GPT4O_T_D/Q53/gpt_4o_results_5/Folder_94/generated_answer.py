def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 41, n + 1):
            sub = s[i:j]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes