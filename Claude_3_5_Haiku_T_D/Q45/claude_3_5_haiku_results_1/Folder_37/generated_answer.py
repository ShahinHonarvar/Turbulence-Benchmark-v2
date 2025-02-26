from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:5] if char.isalpha()]
    palindrome_set = set()
    for perm_length in range(5, len(letters) + 1):
        for perm in permutations(letters, perm_length):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1] and len(candidate) >= 5:
                    palindrome_set.add(candidate)
    return palindrome_set