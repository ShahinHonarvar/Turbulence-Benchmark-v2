def palindrome_of_length_n(s):
    return {s[i:i + 416].lower() for i in range(len(s) - 415) if s[i:i + 416] == s[i:i + 416][::-1].lower() and all((c.isalpha() for c in s[i:i + 416]))}