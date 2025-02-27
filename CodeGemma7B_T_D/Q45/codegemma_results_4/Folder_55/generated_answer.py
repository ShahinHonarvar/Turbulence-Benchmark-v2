from itertools import permutations

def palindromes_between_indices(string):
    ans = set()
    for p in permutations(string[0:3], r=3):
        for a, b, c in permutations(p):
            if a.lower() + b.lower() + c.lower() not in ans:
                ans.add(a.lower() + b.lower() + c.lower())
    return ans