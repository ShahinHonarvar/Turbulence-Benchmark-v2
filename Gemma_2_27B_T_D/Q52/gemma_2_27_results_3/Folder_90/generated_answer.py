def palindrome_of_length_n(s):
    return {s[i:i + 318].lower() for i in range(len(s) - 317) if s[i:i + 318].lower() == s[i:i + 318].lower()[::-1] and s[i:i + 318].isalpha()}