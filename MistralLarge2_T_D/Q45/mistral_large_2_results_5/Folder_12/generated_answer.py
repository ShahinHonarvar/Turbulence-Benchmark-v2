from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:9]))
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            pal = ''.join(perm)
            if pal == pal[::-1]:
                palindromes.add(pal.lower())
    return palindromes