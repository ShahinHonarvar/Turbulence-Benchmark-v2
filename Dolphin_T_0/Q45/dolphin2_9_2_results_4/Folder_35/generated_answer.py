import itertools
    from string import ascii_lowercase

def palindromes_between_indices(s):
    indices_string = s[2:5]
    palindromes = set()
    for p in range(4, len(indices_string) + 1):
        for subset in itertools.combinations(indices_string, p):
            for permutation in itertools.permutations(subset):
                word = ''.join(permutation)
                if word == word[::-1]:
                    palindromes.add(word.lower())
    return palindromes