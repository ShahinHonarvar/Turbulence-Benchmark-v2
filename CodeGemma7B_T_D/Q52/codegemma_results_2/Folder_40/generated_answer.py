def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 3] for i in range(len(s) - 2) if s[i] == s[i + 2]}