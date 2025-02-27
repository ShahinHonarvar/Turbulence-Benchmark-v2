def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    else:
        substring = s[2:4]
        return set((word for word in (''.join(permutation(substring)) for permutation in itertools.permutations(substring, len(substring))) if len(word) >= 3 and word == word[::-1]))