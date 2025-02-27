import itertools

def palindromes_between_indices(string: str) -> set[str]:
    letters = set([char.lower() for char in string[:9] if char.isalpha()])
    palindromes = set()
    for i in range(7, len(letters) + 1):
        for permutation in itertools.permutations(letters, i):
            candidate = ''.join(permutation)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes