from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[2:8].lower()
    letters = [char for char in sub_str if char.isalpha()]
    palindromes = set()
    for perm in set(permutations(letters)):
        candidate = ''.join(perm)
        if len(candidate) >= 6 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes