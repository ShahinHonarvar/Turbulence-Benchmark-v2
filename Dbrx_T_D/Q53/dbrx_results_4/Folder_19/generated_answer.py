def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        s = s.lower()
        return s == s[::-1]
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 1, min(len(s), i + 23)) if is_palindrome(s[i:j])}
    return {p for p in palindromes if p.lower().isalpha()}