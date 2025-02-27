from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    sub_string = s[1:4].lower()
    letters = [ch for ch in sub_string if ch.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes