def palindrome_of_length_n(string):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    length = 78
    palindromes = {string[i:j] for i in range(len(string)) for j in range(i + length, len(string) + 1) if string[i:j] == string[i:j][::-1]}
    return {p for p in palindromes if p}