from itertools import permutations

def palindromes_between_indices(s):
    pals = set()
    for p in permutations(s[4:7], 4):
        for i in range(10):
            pals.add(''.join(p)[::-1])
            p = ''.join(p)[::-1]
            if i % 2 == 0 and p not in pals:
                break
            else:
                pals.add(p)
    return pals