def palindrome_of_length_n(s):
    return {s[i:i + 19].lower() for i in range(len(s) - 18) if s[i:i + 19].lower() == s[i + 18:i - 1:-1].lower()}