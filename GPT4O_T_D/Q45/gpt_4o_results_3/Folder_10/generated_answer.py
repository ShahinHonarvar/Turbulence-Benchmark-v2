from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    english_letters = ''.join(filter(str.isalpha, s))
    generated_permutations = set(permutations(english_letters, len(english_letters)))
    palindromes = set()
    for p in generated_permutations:
        perm = ''.join(p)
        if len(perm) >= 3 and perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes