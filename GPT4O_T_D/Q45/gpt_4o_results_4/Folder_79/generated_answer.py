from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes_set = set()
    for i in range(3, len(s) + 1):
        for perm in permutations(s, i):
            joined = ''.join(perm)
            if joined == joined[::-1]:
                palindromes_set.add(joined)
    return palindromes_set