import itertools

def palindromes_between_indices(s):
    res = set()
    for p in itertools.permutations(s[0:5].lower(), len(s[0:5])):
        for i in range(len(p)):
            for j in range(i + 2, len(p) + 1):
                if p[i:j] == p[i:j][::-1]:
                    res.add(p[i:j])
    return res