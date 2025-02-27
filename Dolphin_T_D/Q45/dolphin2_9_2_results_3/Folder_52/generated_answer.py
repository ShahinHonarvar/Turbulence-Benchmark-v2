from itertools import permutations

def palindromes_between_indices(input_string):
    input_string = input_string[:8]
    input_string = input_string.lower()
    letters = list(set(input_string))
    palindromes = set()
    for p in permutations(letters, 6):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes