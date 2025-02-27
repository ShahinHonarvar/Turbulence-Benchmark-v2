def palindrome_of_length_n(s):
    return {s[i:i + 69].lower() for i in range(len(s) - 68) if s[i:i + 69].lower() == s[i:i + 69].lower()[::-1] and s[i:i + 69].isalpha()}