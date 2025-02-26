from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:7] if c.isalpha()]
    if len(letters) < 7:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters, len(letters))):
        candidate = ''.join(perm)
        if len(candidate) >= 7:
            for i in range(len(candidate) - len(candidate) // 2):
                if candidate[i] != candidate[-(i + 1)]:
                    break
            else:
                unique_palindromes.add(candidate)
    return unique_palindromes