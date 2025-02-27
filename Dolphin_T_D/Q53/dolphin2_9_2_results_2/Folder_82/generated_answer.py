def palindrome_of_length_at_least_n(s):
    s = ''.join((ch for ch in s if ch.isalpha()))
    s = s.lower()
    n = 72
    palindromes = {s[i:i + n] for i in range(len(s) - n + 1)}
    return {p for p in palindromes if p == p[::-1]}