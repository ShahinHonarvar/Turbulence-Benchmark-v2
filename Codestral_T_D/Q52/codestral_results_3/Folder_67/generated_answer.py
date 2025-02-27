def palindrome_of_length_n(s):
    return {s[i:i + 42].lower() for i in range(len(s) - 41) if s[i:i + 42].lower() == s[i:i + 42].lower()[::-1] and s[i:i + 42].isalpha()}