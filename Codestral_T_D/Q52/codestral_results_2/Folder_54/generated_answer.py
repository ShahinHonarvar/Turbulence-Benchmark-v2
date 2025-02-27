def palindrome_of_length_n(s):
    return {s[i:i + 85].lower() for i in range(len(s) - 84) if s[i:i + 85].lower() == s[i:i + 85].lower()[::-1] and s[i:i + 85].isalpha()}