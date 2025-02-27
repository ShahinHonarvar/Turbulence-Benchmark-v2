from itertools import permutations

def palindromes_between_indices(params: str):
    letters = [char.lower() for char in params[4:10]]
    palindromes = set()
    for length in range(5, 11):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes