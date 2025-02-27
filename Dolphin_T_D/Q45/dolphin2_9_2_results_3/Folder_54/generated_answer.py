def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    if len(set(letters)) < 2:
        return set()
    subsets = {}
    for i in range(4, len(s)):
        possible = set()
        for c in letters:
            possible.add(c)
            if c not in subsets:
                subsets[c] = {c}
            else:
                subsets[c].add(c)
        subset_size = len(possible)
        while subset_size > 0:
            for i in range(subset_size):
                if i in possible:
                    possible.remove(i)
                if i not in subsets:
                    subsets[i] = {i}
                else:
                    subsets[i].add(i)
            subset_size = len(possible)
    result = set()
    for subset in subsets.values():
        word = ''.join(sorted(list(subset)))
        result.add(word)
    return result