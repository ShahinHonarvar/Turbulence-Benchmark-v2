def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 78
    return {s[i:j] for i in range(len(s)) for j in range(i + n, len(s) + 1) if s[i:j] == s[i:j][::-1] and s[i:j].isalpha()}