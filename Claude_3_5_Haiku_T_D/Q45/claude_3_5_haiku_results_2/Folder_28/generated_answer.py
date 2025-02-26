from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:6] if char.isalpha()]
    palindrome_set = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for p in set(permutations(perm)):
                candidate = ''.join(p)
                if candidate == candidate[::-1]:
                    palindrome_set.add(candidate)
    return palindrome_set