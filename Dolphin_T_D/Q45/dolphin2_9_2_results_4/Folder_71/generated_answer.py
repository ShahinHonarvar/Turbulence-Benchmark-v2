from itertools import permutations, product

def palindromes_between_indices(s):
    letters = s[1:4]
    palindromes = set()
    for length in range(4, len(s)):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word.lower())
        for perm in product(letters, repeat=length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word.lower())
    return palindromes