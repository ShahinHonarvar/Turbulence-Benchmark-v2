from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([c.lower() for c in text[1:10] if c.isalpha()])
    palindromes = set()
    for i in range(7, len(letters) + 1):
        for perm in permutations(letters, i):
            if ''.join(perm) == ''.join(perm)[::-1]:
                palindromes.add(''.join(perm))
    return palindromes