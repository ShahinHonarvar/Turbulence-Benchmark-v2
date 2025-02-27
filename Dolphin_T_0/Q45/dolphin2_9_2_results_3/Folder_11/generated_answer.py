def palindromes_between_indices(strings):
    letters = set(strings[3:8].lower())
    length = len(letters)
    return set(''.join((letters[i] * (length // 2 - i) + c + letters[i] * (length // 2 - i) for i in range(length // 2) for c in letters)))