def palindromes_between_indices(s):
    letters = set((s[i].lower() for i in range(3, 10) if s[i].isalpha()))
    arrangements = {''.join(permutation).lower() for permutation in itertools.permutations(letters, len(letters))}
    palindromes = {arrangement for arrangement in arrangements if len(arrangement) >= 3 and arrangement == arrangement[::-1]}
    return palindromes