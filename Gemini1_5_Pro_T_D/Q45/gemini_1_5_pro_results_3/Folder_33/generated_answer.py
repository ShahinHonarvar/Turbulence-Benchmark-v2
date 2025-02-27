import itertools

def palindromes_between_indices(string):
    letters = [string[i].lower() for i in range(7, 10) if string[i].isalpha()]
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for permutation in itertools.permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1] and word not in palindromes:
                palindromes.add(word)
    return palindromes