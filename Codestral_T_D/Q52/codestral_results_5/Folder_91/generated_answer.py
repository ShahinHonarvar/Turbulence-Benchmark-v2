def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 7] for i in range(len(s) - 6) if s[i:i + 7] == s[i:i + 7][::-1] and s[i:i + 7].isalpha()}