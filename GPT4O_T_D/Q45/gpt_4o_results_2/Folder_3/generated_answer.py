from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substr = s[7:10].lower()
    letters = ''.join(filter(str.isalpha, substr))
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 3 and word == word[::-1]:
            palindromes.add(word)
    return palindromes