from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:8] if char.isalpha()]
    palindrome_set = set()
    for length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for i in range(len(perm) - length + 1):
                subset = perm[i:i + length]
                if len(subset) >= 6:
                    candidate = ''.join(subset)
                    if candidate == candidate[::-1]:
                        palindrome_set.add(candidate)
    return palindrome_set