def palindrome_of_length_n(s):
    return {s[i:i + 45].lower() for i in range(len(s) - 44) if s[i:i + 45].lower() == s[i:i + 45][::-1].lower() and s[i:i + 45].isalpha()}