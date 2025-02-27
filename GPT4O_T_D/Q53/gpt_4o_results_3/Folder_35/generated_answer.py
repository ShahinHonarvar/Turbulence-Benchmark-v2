def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    found_palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 26, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes