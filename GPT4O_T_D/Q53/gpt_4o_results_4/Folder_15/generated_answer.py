def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(n):
        for j in range(i + 4, n + 1):
            substring = s[i:j]
            if is_palindrome(substring) and substring.isalpha():
                palindromes.add(substring)
    return palindromes