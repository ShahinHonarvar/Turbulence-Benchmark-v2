from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:8] if c.isalpha()]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for perm in set(permutations(letters, len(letters))):
        for i in range(len(perm) // 2):
            if perm[i] != perm[-(i + 1)]:
                break
        else:
            if len(perm) >= 6:
                palindrome = ''.join(perm)
                palindromes.add(palindrome)
    return palindromes