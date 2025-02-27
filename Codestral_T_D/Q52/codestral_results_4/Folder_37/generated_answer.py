def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 84] for i in range(len(s) - 83) if s[i:i + 84] == s[i:i + 84][::-1] and s[i:i + 84].isalpha()}