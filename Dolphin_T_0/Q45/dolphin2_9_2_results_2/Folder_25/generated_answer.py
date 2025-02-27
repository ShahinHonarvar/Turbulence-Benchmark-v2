from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:5]]
    palindromes = set()
    for p in permutations(letters, 3):
        if ''.join(p) == ''.join(p[::-1]) and ''.join(p) not in palindromes:
            palindromes.add(''.join(p))
    return palindromes