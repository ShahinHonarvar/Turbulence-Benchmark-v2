from itertools import permutations

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[4:10] if char.isalpha()]
    palindrome_set = set()
    for length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for candidate in [''.join(perm), ''.join(reversed(perm))]:
                if candidate == candidate[::-1] and len(candidate) >= 6:
                    palindrome_set.add(candidate)
    return palindrome_set