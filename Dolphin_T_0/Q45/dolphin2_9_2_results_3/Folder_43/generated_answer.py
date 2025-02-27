from itertools import permutations

def palindromes_between_indices(s):
    sub = s[2:6].lower()
    palindromes = set()
    for p in range(4, len(sub) + 1):
        for t in permutations(sub, p):
            if ''.join(t) == ''.join(reversed(t)) and len(set(t)) >= 4:
                palindromes.add(''.join(t))
    return palindromes