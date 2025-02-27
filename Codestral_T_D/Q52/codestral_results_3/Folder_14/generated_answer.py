def palindrome_of_length_n(s):
    return {s[i:i + 63].lower() for i in range(len(s) - 62) if s[i:i + 63].lower() == s[i:i + 63].lower()[::-1] and s[i:i + 63].isalpha()}