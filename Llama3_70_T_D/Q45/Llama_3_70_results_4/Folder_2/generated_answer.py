from itertools import permutations

def palindromes_between_indices(s):
    substr = s[1:6].lower()
    substr = ''.join(filter(str.isalpha, substr))
    palindromes = set()
    for perm in permutations(substr, 6):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes