def palindrome_of_length_n(s):
    return {s[i:i + 131] for i in range(len(s) - 130) if s[i:i + 131].lower() == s[i:i + 131][::-1].lower()}