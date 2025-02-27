from itertools import permutations

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[1:8] if char.isalpha()]
    perms = permutations(letters)
    palindromes = set()
    for perm in perms:
        word = ''.join(perm)
        if len(word) >= 3:
            for i in range(len(word)):
                for j in range(i + 3, len(word) + 1):
                    subword = word[i:j]
                    if subword == subword[::-1]:
                        palindromes.add(subword)
    return palindromes