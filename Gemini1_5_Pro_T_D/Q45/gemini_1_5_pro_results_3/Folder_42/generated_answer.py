import itertools

def palindromes_between_indices(string):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    letters = []
    for i in range(6, 10):
        if string[i].lower() in english_letters:
            letters.append(string[i].lower())
    permutations = set([''.join(p) for i in range(3, len(letters) + 1) for p in itertools.permutations(letters, i)])
    palindromes = set()
    for permutation in permutations:
        if permutation == permutation[::-1]:
            palindromes.add(permutation)
    return palindromes