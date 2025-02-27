def palindrome_of_length_n(string):
    string = string.lower()
    string = ''.join((c for c in string if c.isalpha()))
    n = 57
    return set((string[i:j + 1] for i in range(len(string) - n + 1) for j in range(i, len(string) - n + 1) if string[i:j + 1] == string[j:i - 1:-1]))