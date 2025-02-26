from itertools import permutations

def palindromes_between_indices(s):
    letters = s[4:10]
    alpha_letters = [char.lower() for char in letters if char.isalpha()]
    if len(alpha_letters) < 6:
        return set()
    palindrome_set = set()
    for r in range(6, len(alpha_letters) + 1):
        for perm in set(permutations(alpha_letters, r)):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1]:
                    palindrome_set.add(candidate)
    return palindrome_set