def palindrome_of_length_n(s):
    return {s[i:i + 67] for i in range(len(s) - 66) if s[i:i + 67].lower() == s[i:i + 67][::-1].lower()}