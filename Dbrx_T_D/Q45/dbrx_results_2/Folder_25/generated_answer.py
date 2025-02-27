import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[1:5])
    if len(letters) < 2:
        return set()
    palindromes = {i for i in range(len(letters)) if letters[i:i + 3] == letters[i:i + 3][::-1]}
    for length in range(4, len(letters) + 1):
        palindromes.update({i for i in range(len(letters) - length + 1) if letters[i:i + length] == letters[i:i + length][::-1]})
    return {''.join(letters[i:i + length]) for length in range(3, len(palindromes) + 1) for i in palindromes}