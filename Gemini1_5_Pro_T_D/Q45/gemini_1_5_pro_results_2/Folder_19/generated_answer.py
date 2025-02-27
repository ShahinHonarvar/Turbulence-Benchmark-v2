from itertools import permutations

def palindromes_between_indices(string):
    letters = set([c for c in string[1:8] if c.isalpha()])
    output = set()
    for p in [''.join(i) for r in range(1, len(letters) + 1) for i in permutations(letters, r)]:
        if len(p) >= 7 and p.lower() == p[::-1].lower():
            output.add(p.lower())
    return output