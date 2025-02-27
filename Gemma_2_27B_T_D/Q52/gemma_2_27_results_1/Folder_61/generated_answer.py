def palindrome_of_length_n(s):
    return {s[i:i + 74].lower() for i in range(len(s) - 73) if s[i:i + 74].lower() == s[i + 74 - 1:i - 1:-1].lower() and s[i:i + 74].isalpha()}