from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:7] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        for i in range(len(p)):
            for j in range(i + 5, len(p) + 1):
                sub_p = p[i:j]
                if sub_p == sub_p[::-1]:
                    palindromes.add(''.join(sub_p))
    return palindromes