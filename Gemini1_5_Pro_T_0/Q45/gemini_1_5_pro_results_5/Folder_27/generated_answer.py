import itertools

def palindromes_between_indices(string):
    s = string[2:9].lower()
    letters = [letter for letter in s if letter.isalpha()]
    result = set()
    for i in range(6, len(letters) + 1):
        for permutation in itertools.permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1]:
                result.add(word)
    return result