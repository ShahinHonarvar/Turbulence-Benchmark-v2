def palindrome_of_length_n(s):
    return {s[i:i + 21].lower() for i in range(len(s) - 20) if s[i:i + 21].lower() == s[i:i + 21].lower()[::-1]}