from itertools import permutations

def palindromes_between_indices(s):
    letters = s[3:10]
    palindromes = set()
    for p in range(7, 10):
        for subset in permutations(letters, p):
            for arrangement in set((word.lower() for word in permutations(subset))):
                if arrangement == arrangement[::-1]:
                    palindromes.add(arrangement)
    return palindromes