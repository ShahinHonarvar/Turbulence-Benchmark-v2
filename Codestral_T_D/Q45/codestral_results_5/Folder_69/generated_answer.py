from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:4].lower()
    length = len(s)
    palindromes = set()
    for p in permutations(s):
        for i in range(4):
            for j in range(i + 3, length + 1):
                if j - i >= 4 and p[i:j] == p[i:j][::-1]:
                    palindromes.add(''.join(p[i:j]))
    return palindromes