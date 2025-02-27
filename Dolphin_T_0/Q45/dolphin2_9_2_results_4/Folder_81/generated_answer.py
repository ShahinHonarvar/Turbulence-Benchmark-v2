from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7]
    letters = []
    for i in s:
        if i.isalpha():
            letters.append(i.lower())
    palindromes_set = set()
    for p in range(3, len(letters) + 1):
        for t in permutations(letters, p):
            for i in range(p):
                for j in range(i + 1, p):
                    if t[i:j + 1] == t[j:i:-1]:
                        palindromes_set.add(''.join(t[i:j + 1]))
    return palindromes_set