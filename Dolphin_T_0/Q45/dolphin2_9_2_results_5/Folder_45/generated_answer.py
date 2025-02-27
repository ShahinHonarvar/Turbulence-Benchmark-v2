def palindromes_between_indices(s):
    s = s[5:10].lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    subsets = sum((combinations(s, r) for r in range(4, len(s) + 1)), [])
    subsets = [''.join(c) for c in subsets if len(set(c) & vowels) > 0]
    palindromes = [c for c in subsets if c == c[::-1]]
    return set(palindromes)