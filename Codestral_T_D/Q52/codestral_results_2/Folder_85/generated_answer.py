def palindrome_of_length_n(s):
    return {s[i:i + 46].lower() for i in range(len(s) - 45) if s[i:i + 46].lower() == s[i:i + 46].lower()[::-1] and s[i:i + 46].isalpha()}