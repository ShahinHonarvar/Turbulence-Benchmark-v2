from itertools import permutations

def palindromes_between_indices(s):
    letters = set(s.lower()[0:6])
    palindromes = set()
    for i in range(4, 7):
        for perm in permutations(letters, i):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes