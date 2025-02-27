def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 67] for i in range(len(s) - 66) if s[i:i + 67] == s[i:i + 67][::-1] and s[i:i + 67].isalpha()}