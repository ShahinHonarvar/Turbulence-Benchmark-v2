def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 37] for i in range(len(s) - 36) if s[i:i + 37] == s[i:i + 37][::-1] and s[i:i + 37].isalpha()}