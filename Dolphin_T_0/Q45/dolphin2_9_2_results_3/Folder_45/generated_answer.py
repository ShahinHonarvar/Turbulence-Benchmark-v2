import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[5:10] if char.isalpha()]
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for p in itertools.permutations(letters, i):
            if ''.join(p) == ''.join(reversed(p)):
                palindromes.add(''.join(p))
    return palindromes