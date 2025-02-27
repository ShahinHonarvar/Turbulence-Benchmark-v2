def palindrome_of_length_n(s):
    return {s[i:i + 57].lower() for i in range(len(s) - 56) if s[i:i + 57].lower() == s[i:i + 57].lower()[::-1] and s[i:i + 57].isalpha()}