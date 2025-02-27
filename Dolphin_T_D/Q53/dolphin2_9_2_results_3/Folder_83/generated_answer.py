def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 59):
        substring = s[i:i + 60]
        if all((c in 'abcdefghijklmnopqrstuvwxyz' for c in substring)) and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes