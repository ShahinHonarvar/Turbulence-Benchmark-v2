def palindrome_of_length_n(s):
    N = 38
    s = s.lower()
    return {s[i:i + N] for i in range(len(s) - N + 1) if s[i:i + N] == s[i:i + N][::-1] and s[i:i + N].isalpha()}