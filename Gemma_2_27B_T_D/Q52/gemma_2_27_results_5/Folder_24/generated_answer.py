def palindrome_of_length_n(s):
    return {s[i:i + 29] for i in range(len(s) - 28) if s[i:i + 29].lower() == s[i:i + 29][::-1].lower()}