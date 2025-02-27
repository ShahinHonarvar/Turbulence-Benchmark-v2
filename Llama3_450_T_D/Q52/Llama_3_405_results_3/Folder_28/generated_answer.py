def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 43] for i in range(len(s) - 42) if s[i:i + 43] == s[i:i + 43][::-1] and s[i:i + 43].isalpha()}