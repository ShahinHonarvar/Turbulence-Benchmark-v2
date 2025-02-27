def palindrome_of_length_n(string, n=99):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    return {string[i:n + i] for i in range(len(string) - n + 1) if string[i:n + i] == string[i:n + i][::-1]} if n <= len(string) else set()