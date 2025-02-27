from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:8].lower()
    s = ''.join(filter(str.isalpha, s))
    if len(s) < 3:
        return set()
    char_count = Counter(s)
    palindromes = set()
    for length in range(3, len(s) + 1):
        for perm in permutations(s, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes