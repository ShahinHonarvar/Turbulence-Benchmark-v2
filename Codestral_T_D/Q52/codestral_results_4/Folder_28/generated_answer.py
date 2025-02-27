def palindrome_of_length_n(s):
    return {s[i:i + 43] for i in range(len(s) - 42) if s[i:i + 43].lower() == s[i:i + 43].lower()[::-1] and s[i:i + 43].isalpha()}