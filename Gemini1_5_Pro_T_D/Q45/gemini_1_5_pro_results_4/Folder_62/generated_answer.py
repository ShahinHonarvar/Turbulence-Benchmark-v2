from itertools import permutations

def palindromes_between_indices(string):
    letters = set([c for c in string[:9] if c.isalpha()])
    output = set()
    for length in range(7, len(letters) + 1):
        for candidate in permutations(letters, length):
            word = ''.join(candidate)
            if word.lower() == word[::-1].lower():
                output.add(word.lower())
    return output