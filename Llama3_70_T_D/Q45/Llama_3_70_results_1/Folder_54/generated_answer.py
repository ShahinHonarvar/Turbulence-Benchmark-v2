from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:10] if char.isalpha()]
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for p in permutations(letters, i):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes