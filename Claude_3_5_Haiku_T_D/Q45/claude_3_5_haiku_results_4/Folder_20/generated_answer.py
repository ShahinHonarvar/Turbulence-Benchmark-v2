from itertools import permutations

def palindromes_between_indices(s):
    subset = s[2:9].lower()
    letters = [char for char in subset if char.isalpha()]
    palindrome_set = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if len(candidate) >= 4 and candidate == candidate[::-1]:
                    palindrome_set.add(candidate)
    return palindrome_set