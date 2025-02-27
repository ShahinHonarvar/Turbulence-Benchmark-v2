def palindrome_of_length_n(s):
    L = 57
    s = s.lower()
    return {s[i:i + L] for i in range(len(s) - L + 1) if s[i:i + L] == s[i:i + L][::-1] and s[i:i + L].isalpha()}