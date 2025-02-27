from itertools import permutations

def palindromes_between_indices(s):
    letters = []
    for i in range(7):
        if s[i].isalpha():
            letters.append(s[i].lower())
    perms = [''.join(p) for p in permutations(letters)]
    palindromes = set()
    for item in perms:
        if len(item) >= 5 and item == item[::-1]:
            palindromes.add(item)
    return palindromes