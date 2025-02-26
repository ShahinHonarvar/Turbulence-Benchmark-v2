from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:7].lower()
    letters = [char for char in substring if char.isalpha()]
    palindrome_set = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1]:
                    palindrome_set.add(candidate)
    return palindrome_set