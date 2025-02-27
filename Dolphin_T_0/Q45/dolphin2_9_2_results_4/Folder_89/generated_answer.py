def palindromes_between_indices(s):
    letters = [ch for ch in s[5:10] if ch.lower() in 'abcdefghijklmnopqrstuvwxyz']
    if len(''.join(letters)) < 6:
        return set()
    return {''.join(les) + les[::-1] for les in set(''.join(letters).join(map(str, permutations(letters, len(letters)))))}