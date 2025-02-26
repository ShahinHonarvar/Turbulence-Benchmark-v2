from itertools import combinations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:6] if char.isalpha()]
    palindrome_set = set()
    for r in range(5, len(letters) + 1):
        for combo in combinations(letters, r):
            for perm in set(combinations(combo + tuple(reversed(combo)), r * 2 - 1)):
                candidate = ''.join(perm)
                if len(candidate) >= 5 and candidate == candidate[::-1]:
                    palindrome_set.add(candidate)
    return palindrome_set