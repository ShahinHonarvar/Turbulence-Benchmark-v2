import itertools

def palindromes_between_indices(text):
    letters = set()
    for i in range(2, 10):
        if text[i].isalpha():
            letters.add(text[i].lower())
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for permutation in itertools.permutations(letters, i):
            candidate = ''.join(permutation)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes