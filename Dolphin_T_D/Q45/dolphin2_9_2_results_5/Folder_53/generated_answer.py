from itertools import permutations

def palindromes_between_indices(word):
    word = word[4:9]
    word = ''.join([char for char in word if char.isalpha()])
    word = word.lower()
    palindromes = set()
    for i in range(6, len(word) + 1):
        perms = permutations(word, i)
        for perm in perms:
            pal = ''.join(perm)
            if pal == pal[::-1]:
                palindromes.add(pal)
    return palindromes