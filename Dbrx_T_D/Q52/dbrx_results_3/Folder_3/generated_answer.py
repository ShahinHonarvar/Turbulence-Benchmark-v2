def palindrome_of_length_n(string, n=100):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    palindromes = {string[i:j] for i in range(len(string)) for j in range(i + n, len(string) + 1) if string[i:j] == string[i:j][::-1]}
    return palindromes