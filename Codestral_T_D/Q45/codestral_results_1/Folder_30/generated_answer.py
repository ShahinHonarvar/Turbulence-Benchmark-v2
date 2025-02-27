from itertools import permutations

def palindromes_between_indices(string):
    string = string[:5].lower()
    palindromes = set()
    for length in range(4, len(string) + 1):
        for perm in permutations(string, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes