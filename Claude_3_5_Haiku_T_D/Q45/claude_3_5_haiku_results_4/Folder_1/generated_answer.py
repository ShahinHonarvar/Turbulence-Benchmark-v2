from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:8] if char.isalpha()]
    if len(letters) < 5:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 4, len(perm) + 1):
                candidate = perm[i:j]
                if len(candidate) >= 5:
                    full_perm = candidate + candidate[::-1]
                    if len(set(full_perm)) == len(candidate):
                        palindrome_set.add(''.join(full_perm))
    return palindrome_set