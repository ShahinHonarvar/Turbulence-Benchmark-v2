def palindrome_of_length_at_least_n(s):

    def is_palindrome(w):
        return w == w[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    found_palindromes = set()
    for i in range(n):
        for j in range(i + 54, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes