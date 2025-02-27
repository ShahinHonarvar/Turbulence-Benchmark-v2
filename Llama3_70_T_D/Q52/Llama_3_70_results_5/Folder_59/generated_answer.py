def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 39] for i in range(len(s) - 38) if s[i:i + 39] == s[i:i + 39][::-1] and s[i:i + 39].isalpha()}