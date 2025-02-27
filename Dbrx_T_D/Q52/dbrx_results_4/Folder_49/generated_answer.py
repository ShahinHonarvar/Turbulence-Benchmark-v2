def palindrome_of_length_n(string, n=47):
    string = ''.join((e for e in string.lower() if e.isalpha()))
    return {string[i:j] for i in range(len(string)) for j in range(i + n, len(string) + 1) if string[i:j] == string[i:j][::-1]}