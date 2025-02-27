from itertools import permutations

def palindromes_between_indices(s):
    target_substring = ''.join((c.lower() for c in s[2:10] if c.isalpha()))
    possible_palindromes = set()
    for p in permutations(target_substring):
        if len(p) >= 7 and p == p[::-1]:
            possible_palindromes.add(''.join(p))
    return possible_palindromes