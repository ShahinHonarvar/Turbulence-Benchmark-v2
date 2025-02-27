def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        s = s.lower()
        return s == s[::-1]
    palindromes = {p for p in {s[i:j] for i in range(len(s)) for j in range(i + 1, min(len(s), i + 89) + 1)} if is_palindrome(p)}
    return palindromes