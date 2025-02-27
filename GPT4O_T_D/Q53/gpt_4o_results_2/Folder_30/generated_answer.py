def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = ''.join(filter(str.isalpha, s.lower()))
    found_palindromes = set()
    n = 16
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes