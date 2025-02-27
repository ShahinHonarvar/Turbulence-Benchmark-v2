def palindrome_of_length_n(s):
    return {s[i:i + 91].lower() for i in range(len(s) - 90) if s[i:i + 91].lower() == s[i:i + 91][::-1].lower() and s[i:i + 91].isalpha()}