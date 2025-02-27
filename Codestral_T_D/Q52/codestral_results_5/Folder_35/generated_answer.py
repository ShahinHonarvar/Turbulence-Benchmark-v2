def palindrome_of_length_n(s):
    return {s[i:i + 116].lower() for i in range(len(s) - 115) if s[i:i + 116].lower() == s[i:i + 116].lower()[::-1] and s[i:i + 116].isalpha()}