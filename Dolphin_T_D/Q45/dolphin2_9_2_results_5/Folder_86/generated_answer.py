import itertools

def palindromes_between_indices(string):
    string = string[6:10]
    string_lower = string.lower()
    palindromes = set()
    for i in range(4, len(string_lower) + 1):
        for perm in itertools.permutations(string_lower, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes