def palindrome_of_length_n(s):
    return {s[i:i + 18].lower() for i in range(len(s) - 18) if s[i:i + 18].lower() == s[i:i + 18].lower()[::-1] and s[i:i + 18].isalpha()}