def palindrome_of_length_n(s):
    return {s[i:i + 25].lower() for i in range(len(s) - 24) if s[i:i + 25].lower() == s[i:i + 25].lower()[::-1] and s[i:i + 25].isalpha()}