def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 77] for i in range(len(s) - 76) if s[i:i + 77] == s[i:i + 77][::-1] and s[i:i + 77].isalpha()}