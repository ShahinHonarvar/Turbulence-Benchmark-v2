def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        s = ''.join((c.lower() for c in s if c.isalpha()))
        return s == s[::-1]
    return {s[i:j] for i in range(40, 95) for j in range(i + 45, i + 52) if is_palindrome(s[i:j])}