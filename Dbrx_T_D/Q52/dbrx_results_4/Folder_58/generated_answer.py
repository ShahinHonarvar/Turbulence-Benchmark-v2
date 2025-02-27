def palindrome_of_length_n(string, n=223):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    if n > len(string) or n <= 0:
        return set()
    return {string[i:j] for i in range(len(string)) for j in range(i + n, len(string) + 1) if string[i:j] == string[i:j][::-1]}