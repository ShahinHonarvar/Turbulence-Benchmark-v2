import itertools

def palindromes_between_indices(string):
    letters = set([c.lower() for c in string[1:9] if c.isalpha()])
    result = set()
    for i in range(6, len(letters) + 1):
        for permutation in itertools.permutations(letters, i):
            candidate = ''.join(permutation)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result