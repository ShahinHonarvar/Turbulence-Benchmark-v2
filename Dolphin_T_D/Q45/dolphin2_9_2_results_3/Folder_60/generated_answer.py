import itertools

def palindromes_between_indices(s):
    letters = set(''.join((s[i] for i in range(3, 7) if s[i].isalpha())))
    len_letters = len(letters)
    palindromes = set()
    if len_letters < 4:
        return palindromes
    for i in range(len_letters, 0, -1):
        for subset in itertools.combinations(letters, i):
            for p in itertools.permutations(subset):
                pal = ''.join(p)
                if pal == pal[::-1]:
                    palindromes.add(pal.lower())
    return palindromes