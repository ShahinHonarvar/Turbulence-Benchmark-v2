def palindrome_of_length_n(s):
    return {s[i:i + 49].lower() for i in range(len(s) - 48) if s[i:i + 49].lower() == s[i:i + 49].lower()[::-1]}