def palindromes_between_indices(s):

    def is_palindrome(s):
        s = s.lower()
        return s == s[::-1]
    s = s[3:8]
    palindromes = {p for p in {s[i:j] for i in range(len(s)) for j in range(i + 5, len(s) + 1)} if is_palindrome(p)}
    return palindromes