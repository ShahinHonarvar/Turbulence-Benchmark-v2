def palindrome_of_length_n(string, n=464):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    if len(string) < n:
        return set()
    return {string[i:i + n] for i in range(len(string) - n + 1) if string[i:i + n] == string[i:i + n][::-1] and string[i:i + n].isalpha()}