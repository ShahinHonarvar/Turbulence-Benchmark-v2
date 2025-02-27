def palindrome_of_length_n(s):
    return {s[i:i + 289].lower() for i in range(len(s) - 288) if s[i:i + 289].lower() == s[i:i + 289].lower()[::-1] and s[i:i + 289].isalpha()}