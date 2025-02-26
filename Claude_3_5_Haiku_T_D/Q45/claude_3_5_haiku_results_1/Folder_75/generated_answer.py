from itertools import combinations, permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:5] if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combo in _generate_combinations(letters, length):
            if _is_palindrome(combo):
                palindromes.add(''.join(combo))
    return palindromes

def _generate_combinations(letters, length):
    all_permutations = set()
    for combo in combinations(letters, length):
        all_permutations.update(permutations(combo))
    return all_permutations

def _is_palindrome(combo):
    return list(combo) == list(reversed(combo))