from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:3] if c.isalpha()]
    palindrome_set = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for combo in set(permutations(perm)):
                if combo == combo[::-1]:
                    palindrome_set.add(''.join(combo))
    return palindrome_set