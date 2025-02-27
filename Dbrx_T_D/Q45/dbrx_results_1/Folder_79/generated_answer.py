import string

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s if c.lower() in string.ascii_letters))[1:8]
    palindromes = {letters[i:j + 1] for i in range(len(letters)) for j in range(i, len(letters)) if letters[i:j + 1] == letters[i:j + 1][::-1]}
    return {p for p in palindromes if len(p) >= 3}