import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[8:10] if c.isalpha()]
    letters = [c.lower() for c in letters]
    letters_count = {c: letters.count(c) for c in letters}
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in itertools.combinations_with_replacement(letters, r):
            p = ''.join(p)
            if p == p[::-1] and all((p.count(c) <= letters_count[c] for c in p)):
                palindromes.add(p)
    return palindromes