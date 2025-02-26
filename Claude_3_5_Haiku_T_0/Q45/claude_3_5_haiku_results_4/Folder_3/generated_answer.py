from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[7:10] if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 2, len(perm) + 1):
                candidate = perm[i:j]
                if len(candidate) >= 3 and list(candidate) == list(candidate)[::-1]:
                    palindrome_set.add(''.join(candidate))
    return palindrome_set