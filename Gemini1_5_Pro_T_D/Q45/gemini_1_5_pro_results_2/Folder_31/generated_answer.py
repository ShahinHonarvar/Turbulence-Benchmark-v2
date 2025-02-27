import itertools

def palindromes_between_indices(string):
    letters = ''.join((char for char in string[1:9] if char.isalpha())).lower()
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for combination in itertools.permutations(letters, i):
            word = ''.join(combination)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes