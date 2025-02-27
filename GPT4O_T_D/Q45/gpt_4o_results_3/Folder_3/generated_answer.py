from itertools import permutations

def palindromes_between_indices(s):
    s = s[7:10].lower()
    s_letters = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for perm in permutations(s_letters):
        candidate = ''.join(perm)
        if len(candidate) >= 3 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes