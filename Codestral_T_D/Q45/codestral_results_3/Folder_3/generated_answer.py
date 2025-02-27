from itertools import permutations

def palindromes_between_indices(s):
    sub_s = s[7:10].lower()
    palindromes = set()
    for i in range(3, len(sub_s) + 1):
        for p in set(permutations(sub_s, i)):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes