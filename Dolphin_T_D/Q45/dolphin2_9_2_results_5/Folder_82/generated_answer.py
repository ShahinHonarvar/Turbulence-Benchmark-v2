import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:7]]
    perms = list(set(itertools.permutations(letters)))
    palindrome_lengths = range(7, 13)
    palindromes = set()
    for perm in perms:
        for length in palindrome_lengths:
            for i in range(len(perm) - length + 1):
                pal = perm[i:i + length]
                if pal == pal[::-1]:
                    palindromes.add(''.join(pal))
    return palindromes