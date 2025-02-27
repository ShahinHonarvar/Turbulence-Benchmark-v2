from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(s):
    s = s[2:9].lower()
    palindromes = {p for p in set((''.join(p) for p in permutations(s, 6) if set(p).issubset(ascii_lowercase))) if p == p[::-1]}
    for i in range(7, 10):
        for p in permutations(s, i):
            p = ''.join(p)
            if set(p).issubset(ascii_lowercase) and p == p[::-1]:
                palindromes.add(p)
    return palindromes