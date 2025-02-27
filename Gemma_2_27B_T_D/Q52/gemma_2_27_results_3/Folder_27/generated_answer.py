def palindrome_of_length_n(s):
    return {s[i:i + 56].lower() for i in range(len(s) - 55) if s[i:i + 56].lower() == s[i:i + 56][::-1].lower()}