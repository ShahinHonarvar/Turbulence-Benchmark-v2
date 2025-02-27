def palindrome_of_length_n(s):
    return {s[i:i + 95].lower() for i in range(len(s) - 94) if s[i:i + 95].lower() == s[i:i + 95][::-1]}