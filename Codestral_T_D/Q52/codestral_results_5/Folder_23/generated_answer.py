def palindrome_of_length_n(s):
    n = 69
    return {s[i:i + n] for i in range(len(s) - n + 1) if s[i:i + n].lower() == s[i:i + n].lower()[::-1] and s[i:i + n].isalpha()}