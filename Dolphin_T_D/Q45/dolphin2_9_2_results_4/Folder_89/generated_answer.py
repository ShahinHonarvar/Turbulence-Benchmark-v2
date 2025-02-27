import itertools

def palindromes_between_indices(string):
    indices = string[5:10]
    letters = [char for char in indices if char.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in itertools.permutations(letters, length):
            word = ''.join(perm)
            if word == word.lower() and word == word[::-1].lower():
                palindromes.add(word)
    return palindromes