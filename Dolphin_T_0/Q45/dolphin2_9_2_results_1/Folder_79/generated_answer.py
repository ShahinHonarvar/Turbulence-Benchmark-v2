from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8].replace(' ', '').lower()
    len_s = len(s)
    palindromes = set()
    for i in range(len_s):
        for j in range(i + 2, len_s + 1):
            sub = s[i:j]
            perms = [''.join(p) for p in permutations(sub)]
            for perm in perms:
                if perm == perm[::-1]:
                    palindromes.add(perm)
    return palindromes