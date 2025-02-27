import string

def palindrome_of_length_n(text):
    letters = set(string.ascii_lowercase)
    palindromes = set()
    text = text.lower()
    n = 96
    for i in range(len(text) - n + 1):
        s = text[i:i + n]
        if len(set(s).difference(letters)) == 0:
            if s == s[::-1]:
                palindromes.add(s)
    return palindromes