def palindromes_between_indices(text):
    text = text[5:9]
    if len(text) < 4:
        return set()
    sets = [set(i) for i in set(text)]
    if len(sets) < 4:
        return set()
    for i in range(len(sets)):
        sets[i] = ''.join(sorted(sets[i]))
    sets.sort(key=len)
    return sets