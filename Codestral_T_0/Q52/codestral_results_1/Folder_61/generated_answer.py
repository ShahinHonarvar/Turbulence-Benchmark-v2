def palindrome_of_length_n(s):
    s = s.lower()
    n = 74
    return {s[i:i + n] for i in range(len(s) - n + 1) if s[i:i + n] == s[i:i + n][::-1] and s[i:i + n].isalpha()}