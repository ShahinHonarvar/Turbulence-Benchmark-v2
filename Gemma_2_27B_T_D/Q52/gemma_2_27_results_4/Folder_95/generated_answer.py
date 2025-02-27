def palindrome_of_length_n(s):
    return {s[i:i + 87].lower() for i in range(len(s) - 86) if s[i:i + 87].lower() == s[i + 86:i:-1].lower() and s[i:i + 87].isalpha()}