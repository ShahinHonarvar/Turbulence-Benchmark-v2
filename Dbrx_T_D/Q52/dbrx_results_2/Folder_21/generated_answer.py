def palindrome_of_length_n(string, n=407):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    return {substring for i in range(len(string) - n + 1) for substring in (string[i:i + n],) if substring == substring[::-1]}