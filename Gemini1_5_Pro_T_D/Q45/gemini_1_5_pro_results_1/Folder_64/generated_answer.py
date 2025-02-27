from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[4:10]
    pat = ''
    for i in s:
        if i.isalpha():
            pat = pat + i
    for i in range(5, len(pat) + 1):
        perm = permutations(pat.lower(), i)
        for i in list(perm):
            a = ''.join(i)
            if a == a[::-1] and len(a) >= 5:
                result.add(a)
    return result