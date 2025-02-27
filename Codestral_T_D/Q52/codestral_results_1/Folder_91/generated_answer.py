def palindrome_of_length_n(s):
    return {s[i:i + 7] for i in range(len(s) - 6) if s[i:i + 7].lower() == s[i:i + 7].lower()[::-1] and s[i:i + 7].isalpha()}