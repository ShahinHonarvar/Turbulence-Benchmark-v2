from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:7] if char.isalpha()]
    if len(letters) < 5:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm) - 4):
            candidate = perm[i:i + 5]
            if candidate == candidate[::-1]:
                palindrome_set.add(''.join(candidate))
    return palindrome_set