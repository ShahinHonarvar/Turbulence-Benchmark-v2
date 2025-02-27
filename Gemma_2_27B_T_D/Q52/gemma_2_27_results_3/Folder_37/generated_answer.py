def palindrome_of_length_n(s):
    return {s[i:i + 84].lower() for i in range(len(s) - 83) if s[i:i + 84].lower() == s[i:i + 84][::-1].lower() and s[i:i + 84].isalpha()}