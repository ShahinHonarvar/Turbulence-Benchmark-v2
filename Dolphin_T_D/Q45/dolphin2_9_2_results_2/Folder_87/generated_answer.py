from itertools import combinations

def palindromes_between_indices(s):
    letters = [c for c in s[3:10] if c.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for comb in combinations(letters, r):
            for p in [''.join(comb[i:r - i]) for i in range(r // 2)]:
                reversed_p = p[::-1].lower()
                if reversed_p in palindromes:
                    palindromes.remove(reversed_p)
                    palindromes.add(p.lower())
                elif p.lower() == reversed_p:
                    palindromes.add(p.lower())
    return palindromes