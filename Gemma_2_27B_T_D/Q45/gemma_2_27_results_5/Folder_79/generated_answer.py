def palindromes_between_indices(text):
    letters = ''.join([c for c in text[1:8] if c.isalpha()]).lower()
    return set([''.join(p) for p in [list(pair) for pair in [(x, y) for y in range(len(letters) - 1, 1, -1) for x in range(y)]] if ''.join(p) == ''.join(p[::-1]) and len(''.join(p)) >= 3])