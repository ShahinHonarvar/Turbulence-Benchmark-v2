def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 2, n + 1):
            substring = s[i:j].lower()
            if all((x in 'abcdefghijklmnopqrstuvwxyz' for x in substring)) and len(substring) >= 54 and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes