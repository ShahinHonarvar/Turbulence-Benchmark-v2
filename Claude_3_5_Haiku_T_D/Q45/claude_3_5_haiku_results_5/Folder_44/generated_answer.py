from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:8] if char.isalpha()]
    palindrome_set = set()
    for r in range(3, len(letters) + 1):
        for perm in set(permutations(letters, r)):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1]:
                    palindrome_set.add(candidate)
    return palindrome_set