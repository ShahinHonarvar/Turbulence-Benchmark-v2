from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(4):
        if string[i].isalpha() and string[i].lower() not in letters:
            letters.append(string[i].lower())
    perms = [''.join(p) for i in range(3, len(letters) + 1) for p in permutations(letters, i)]
    palindromes = set()
    for perm in perms:
        if perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes