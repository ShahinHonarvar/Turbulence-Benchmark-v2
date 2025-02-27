from itertools import permutations

def palindromes_between_indices(string):
    substring = string[2:9].lower()
    palindromes = set()
    for length in range(7, len(substring) + 1):
        for perm in permutations(substring, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes