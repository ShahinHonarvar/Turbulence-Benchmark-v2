def palindrome_of_length_n(s):
    return {s[i:i + 54].lower() for i in range(len(s) - 53) if s[i:i + 54].lower() == s[i + 53:i:-1].lower() and s[i:i + 54].isalpha()}