def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 7
    return {s[i:j + 1] for i in range(len(s)) for j in range(i + n - 1, len(s)) if s[i:j + 1] == s[i:j + 1][::-1] and s[i:j + 1].isalpha()}