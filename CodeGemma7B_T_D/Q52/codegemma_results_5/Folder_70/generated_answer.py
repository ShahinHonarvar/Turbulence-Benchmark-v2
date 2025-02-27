def palindrome_of_length_n(string):
    s = string.lower()
    return {substring for substring in [s[i:i + 401] for i in range(len(s) - 401 + 1)] if substring == substring[::-1]}