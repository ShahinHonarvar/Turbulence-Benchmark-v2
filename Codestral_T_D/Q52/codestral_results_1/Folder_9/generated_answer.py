def palindrome_of_length_n(s):
    return {s[i:i + 72].lower() for i in range(len(s) - 71) if s[i:i + 72].lower() == s[i:i + 72].lower()[::-1] and s[i:i + 72].isalpha()}