from itertools import permutations
    import re

def palindromes_between_indices(s):
    s = re.sub('[^a-zA-Z]', '', s[:7])
    s = s.lower()
    palindromes = set()
    for p in permutations(s):
        for i in range(len(p)):
            for j in range(i, len(p)):
                if p[i:j + 1] == p[i:j + 1][::-1] and len(p[i:j + 1]) >= 7:
                    palindromes.add(p[i:j + 1])
    return palindromes