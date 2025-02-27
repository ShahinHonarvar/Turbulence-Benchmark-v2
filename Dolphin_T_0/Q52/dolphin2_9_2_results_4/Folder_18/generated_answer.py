import string

def palindrome_of_length_n(s):
    letters = set(string.ascii_lowercase)
    length_n = 392
    s = ''.join([c for c in s if c in letters])
    possibilities = {s[i:j] for i in range(len(s)) for j in range(i + length_n, len(s) + 1)}
    palindromes = {p for p in possibilities if p == p[::-1]}
    return palindromes