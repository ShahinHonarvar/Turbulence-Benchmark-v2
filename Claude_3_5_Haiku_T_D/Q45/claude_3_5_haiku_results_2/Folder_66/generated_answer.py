from itertools import permutations

def palindromes_between_indices(s):
    relevant_chars = [char.lower() for char in s[:6] if char.isalpha()]
    palindromes = set()
    for perm_length in range(5, len(relevant_chars) + 1):
        for perm in permutations(relevant_chars, perm_length):
            for start in range(len(perm) - perm_length + 1):
                subset = perm[start:start + perm_length]
                if list(subset) == list(subset)[::-1]:
                    palindromes.add(''.join(subset))
    return palindromes