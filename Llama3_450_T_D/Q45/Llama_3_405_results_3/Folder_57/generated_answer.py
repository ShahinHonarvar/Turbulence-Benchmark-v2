import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:6] if char.isalpha()]
    letters_set = set(letters)
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                p = ''.join(perm)
                if p == p[::-1]:
                    palindromes.add(p)
    return palindromes