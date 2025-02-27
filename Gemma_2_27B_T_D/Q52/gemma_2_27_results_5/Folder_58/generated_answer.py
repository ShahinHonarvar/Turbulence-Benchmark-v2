def palindrome_of_length_n(s):
    return {s[i:i + 223].lower() for i in range(len(s) - 222) if s[i:i + 223].lower() == s[i:i + 223][::-1].lower() and s[i:i + 223].isalpha()}