from string import ascii_letters

def palindromes_between_indices(s):
    pals = set()
    str = s[4:6].lower()
    for p in range(3, len(str) + 1):
        for subset in combinations(str, p):
            word = ''.join(sorted(subset))
            for i in permutations(word):
                pal = ''.join(i)
                if pal == pal[::-1]:
                    pals.add(pal)
    return pals