def palindrome_of_length_n(s):
    return {s[i:i + 407] for i in range(len(s) - 406) if s[i:i + 407].lower() == s[i:i + 407][::-1].lower()}