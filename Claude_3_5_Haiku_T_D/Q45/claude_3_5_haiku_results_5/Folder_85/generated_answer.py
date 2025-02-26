from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:9] if char.isalpha()]
    if len(letters) < 7:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters, 7)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            palindrome_set.add(candidate)
    return palindrome_set