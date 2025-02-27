import itertools

def palindromes_between_indices(string):
    letters = set()
    for i in range(1, 9):
        if i <= len(string) and string[i - 1].isalpha():
            letters.add(string[i - 1].lower())
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for j in itertools.permutations(letters, i):
            word = ''.join(j)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes