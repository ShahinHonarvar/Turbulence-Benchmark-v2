from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:5] if char.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if len(candidate) >= 4 and candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes