def palindrome_of_length_n(s):
    return {s[i:i + 28].lower() for i in range(len(s) - 28) if s[i:i + 28].lower() == s[i:i + 28].lower()[::-1] and s[i:i + 28].isalpha()}