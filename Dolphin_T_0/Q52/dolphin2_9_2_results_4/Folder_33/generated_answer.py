def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = ''.join((c for c in s if c.isalpha()))
    s = ''.join((c for c in s.lower()))
    n = 475
    all_substrings = {s[i:i + n] for i in range(len(s) - n + 1)}
    palindromes = {word for word in all_substrings if is_palindrome(word)}
    return palindromes