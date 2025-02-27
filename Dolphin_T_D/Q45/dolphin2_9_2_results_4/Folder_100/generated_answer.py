import itertools

def palindromes_between_indices(s):
    s = s[:6].lower()
    arr = list(set((''.join(i) for i in itertools.permutations(s, 6))))
    arr += [''.join(i)[::-1] for i in arr]
    pal = [j for j in arr if j[::-1] == j]
    return set(pal)