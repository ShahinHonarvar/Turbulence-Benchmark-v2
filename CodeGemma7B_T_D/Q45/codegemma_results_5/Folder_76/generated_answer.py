from itertools import permutations

def palindromes_between_indices(s):
    OptimizedSet = set()
    for count, char in enumerate(s[1:4]):
        if char.isalpha():
            if count == 0:
                OptimizedSet |= {''.join(p) for p in permutations(list(s[1:5]), 4)}
            elif count == 1:
                OptimizedSet |= {''.join(list(p)) + s[4] + s[2] + s[3] for p in permutations(list(s[1:4]), 3)}
            elif count == 2:
                OptimizedSet |= {''.join(list(p)) + s[4] + s[2] + s[3] for p in permutations(list(s[1:3]), 2)}
            elif count == 3:
                OptimizedSet |= {''.join(p) + s[4] + s[2] + s[3] for p in permutations(list(s[1:4]), 4)}
    if OptimizedSet == set():
        OptimizedSet |= {''.join(p) + s[4] + s[2] + s[3] for p in permutations(list(s[1:5]), 4)}
    if OptimizedSet == set():
        return OptimizedSet
    return OptimizedSet