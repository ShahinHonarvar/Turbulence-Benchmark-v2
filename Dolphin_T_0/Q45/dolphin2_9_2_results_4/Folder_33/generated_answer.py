def palindromes_between_indices(s):
    letters = [char.lower() for char in s[7:10]]
    return {''.join(letters[i:j + 1]) for i in range(len(letters)) for j in range(i, len(letters)) if letters[i:j + 1] == list(reversed(letters[i:j + 1])) and len(letters[i:j + 1]) >= 4}