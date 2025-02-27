def palindrome_of_length_n(s):
    n = 37
    return {s[i:i + n] for i in range(len(s) - n + 1) if s[i:i + n].lower() == s[i:i + n][::-1].lower()}