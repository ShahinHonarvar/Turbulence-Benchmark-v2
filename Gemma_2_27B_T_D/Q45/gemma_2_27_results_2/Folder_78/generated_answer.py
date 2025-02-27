def palindromes_between_indices(text):
    letters = ''.join((char for char in text[6:9] if char.isalpha()))
    return set((p for p in [''.join(t) for t in itertools.permutations(letters)] if len(p) >= 3 and p.lower() == p[::-1].lower()))