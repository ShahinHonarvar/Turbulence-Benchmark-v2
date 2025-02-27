def palindrome_of_length_n(s):
    return {s[i:i + 34].lower() for i in range(len(s) - 33) if s[i:i + 34].lower() == s[i:i + 34].lower()[::-1] and s[i:i + 34].isalpha()}