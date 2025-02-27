from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    s_segment = s[6:10]
    letters = [char.lower() for char in s_segment if char.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes