from itertools import permutations

def palindromes_between_indices(string):
    substring = ''.join(filter(str.isalpha, string[4:9])).lower()
    palindromes = set()
    for length in range(5, len(substring) + 1):
        for perm in permutations(substring, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes