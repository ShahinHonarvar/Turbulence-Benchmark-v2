def palindromes_between_indices(str):
    letters = [str[i] for i in range(3, 10) if str[i].isalpha()]
    return set([''.join(p) for p in itertools.permutations(letters) if len(p) >= 3])