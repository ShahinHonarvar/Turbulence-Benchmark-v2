import itertools

def palindromes_between_indices(string):
    substring = string[6:10].lower()
    palindromes = set()
    for perm in itertools.permutations(substring, 5):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes