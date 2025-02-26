from itertools import permutations

def palindromes_between_indices(s):
    sub_letters = ''.join((c.lower() for c in s[4:6] if c.isalpha()))
    palindromes = set()
    for length in range(3, len(sub_letters) + 1):
        for perm in set(permutations(sub_letters, length)):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes