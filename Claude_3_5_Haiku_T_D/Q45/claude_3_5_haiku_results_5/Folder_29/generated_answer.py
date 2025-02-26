from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:10] if c.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for i in range(length // 2 + 1):
                current_perm = list(perm)
                current_perm[length - 1 - i], current_perm[i] = (current_perm[i], current_perm[length - 1 - i])
                if current_perm == current_perm[::-1]:
                    palindromes.add(''.join(current_perm))
                    break
    return palindromes