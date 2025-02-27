def palindromes_between_indices(text):
    letters = ''.join([c for c in text[5:8] if c.isalpha()]).lower()
    return {''.join(p) for p in [[c] * i for i in range(3, len(letters) + 1) for c in letters] if ''.join(p) == ''.join(p[::-1])}