import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s if c.isalpha() and 0 <= s.index(c) <= 7]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for subset in itertools.combinations(letters, length):
            for perm in itertools.permutations(subset):
                string = ''.join(perm)
                if string == string[::-1] and len(string) >= 6:
                    palindromes.add(string)
    return palindromes