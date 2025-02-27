def palindrome_of_length_n(s):
    return {s[i:i + 472] for i in range(len(s) - 471) if s[i:i + 472].lower() == s[i:i + 472].lower()[::-1] and s[i:i + 472].isalpha()}