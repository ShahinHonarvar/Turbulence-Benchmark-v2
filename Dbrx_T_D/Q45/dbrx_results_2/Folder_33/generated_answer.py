import re

def palindromes_between_indices(s):
    string = s[7:10].lower()
    letters = ''.join(re.findall('[a-z]', string))
    if len(letters) < 4:
        return set()
    palindromes = {letters[i:j + 1] for i in range(len(letters)) for j in range(i, len(letters)) if letters[i:j + 1] == letters[i:j + 1][::-1]}
    return {p for p in palindromes if len(p) >= 4}