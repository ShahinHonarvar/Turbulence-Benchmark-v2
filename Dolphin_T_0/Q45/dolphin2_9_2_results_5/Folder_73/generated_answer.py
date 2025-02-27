def palindromes_between_indices(s):
    letters = [c for c in s[3:7] if c.isalpha()]
    combinations = set(itertools.permutations(letters, 3))
    palindromes = {c for c in combinations if str(c) == str(c[::-1])}
    return palindromes