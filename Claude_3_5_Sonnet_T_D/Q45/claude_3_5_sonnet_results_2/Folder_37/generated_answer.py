import itertools

def palindromes_between_indices(input_string):
    letters = [c.lower() for c in input_string[1:5] if c.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in itertools.permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes