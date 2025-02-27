from itertools import permutations

def palindromes_between_indices(s):
    letters = s[8:10]
    for char in letters:
        if not char.isalpha():
            letters = letters.replace(char, '')
    letters = letters.lower()
    if len(letters) < 3:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for perm in permutations(letters, i + 1):
            if ''.join(perm) == ''.join(perm)[::-1]:
                palindromes.add(''.join(perm))
    return palindromes