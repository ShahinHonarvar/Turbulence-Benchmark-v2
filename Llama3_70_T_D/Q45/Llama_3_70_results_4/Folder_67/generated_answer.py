def palindromes_between_indices(s):
    sub_s = ''.join(filter(str.isalpha, s[2:7])).lower()
    palindromes = set()
    for i in range(5, len(sub_s) + 1):
        for p in itertools.permutations(sub_s, i):
            w = ''.join(p)
            if w == w[::-1]:
                palindromes.add(w)
    return palindromes