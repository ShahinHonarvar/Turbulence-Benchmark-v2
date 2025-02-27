from itertools import permutations

def palindromes_between_indices(string):
    letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_string = ''.join((char for char in string[1:7] if char.lower() in letters))
    palindromes = set()
    for length in range(6, len(filtered_string) + 1):
        for permutation in permutations(filtered_string, length):
            word = ''.join(permutation).lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes