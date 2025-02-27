def palindrome_of_length_n(s):
    return {s[i:i + 9].lower() for i in range(len(s) - 8) if s[i:i + 9].lower() == s[i:i + 9].lower()[::-1] and s[i:i + 9].isalpha()}