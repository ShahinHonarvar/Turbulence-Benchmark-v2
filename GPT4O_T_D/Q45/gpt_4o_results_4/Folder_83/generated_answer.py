from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters_only = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for perm in permutations(letters_only):
        candidate = ''.join(perm)
        if len(candidate) >= 7 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes