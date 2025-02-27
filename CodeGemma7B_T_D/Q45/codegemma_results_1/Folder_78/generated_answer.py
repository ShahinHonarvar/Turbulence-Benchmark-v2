def palindromes_between_indices(txt: str) -> set[str]:
    txt = txt.lower()
    substring = txt[6:9]
    substring = ''.join((c for c in substring if c.isalpha()))
    if len(substring) >= 3:
        permutations = []
        for permutation in permutations_with_repetition(substring):
            permutations.append(''.join(permutation))
        return set(filter(lambda x: x == x[::-1], permutations))
    else:
        return set()

def permutations_with_repetition(lst):
    if len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            for perm in permutations_with_repetition(lst[:i] + lst[i + 1:]):
                yield ([lst[i]] + perm)