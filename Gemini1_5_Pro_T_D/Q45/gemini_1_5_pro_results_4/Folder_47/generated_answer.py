import itertools

def palindromes_between_indices(string):
    s = string[3:8].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for permutation in itertools.permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1] and word not in palindromes:
                palindromes.add(word)
    return palindromes