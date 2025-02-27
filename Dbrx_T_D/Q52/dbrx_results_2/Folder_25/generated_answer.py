def palindrome_of_length_n(string, n=90):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    return {substring for substring in {string[i:j] for i in range(len(string)) for j in range(i + n, len(string) + 1)} if substring == substring[::-1]}