def palindrome_of_length_n(s):
    return {s[i:i + 64].lower() for i in range(len(s) - 63) if s[i:i + 64].lower() == s[i:i + 64].lower()[::-1]}