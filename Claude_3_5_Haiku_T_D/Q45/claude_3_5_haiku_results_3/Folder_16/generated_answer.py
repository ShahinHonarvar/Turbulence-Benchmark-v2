from itertools import permutations

def palindromes_between_indices(s):
    letters = s[6:10].lower()
    alpha_letters = [char for char in letters if char.isalpha()]
    if len(alpha_letters) < 5:
        return set()
    palindromes = set()
    for perm in set(permutations(alpha_letters, 5)):
        for length in range(5, len(perm) + 1):
            for combo in set(permutations(perm, length)):
                forward = ''.join(combo)
                backward = forward[::-1]
                if forward == backward:
                    palindromes.add(forward)
    return palindromes