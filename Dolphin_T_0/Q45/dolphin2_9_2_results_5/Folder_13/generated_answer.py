def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:10]))
    return {p for p in (''.join(i) for i in itertools.permutations(letters, 5)) if p.lower() == p.lower()[::-1]}