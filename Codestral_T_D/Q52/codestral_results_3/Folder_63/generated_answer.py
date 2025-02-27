def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 18] for i in range(len(s) - 18) if s[i:i + 18] == s[i:i + 18][::-1] and s[i:i + 18].isalpha()}