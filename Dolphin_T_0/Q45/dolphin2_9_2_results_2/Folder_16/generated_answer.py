import itertools

def palindromes_between_indices(string):
    substring = string[6:10]
    letters = ''.join((c for c in substring if c.isalpha()))
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for perm in itertools.permutations(letters, i):
            for p in palindrome_partitions(perm):
                if len(''.join(p)) >= 5:
                    palindromes.add(''.join(p).lower())
    return palindromes