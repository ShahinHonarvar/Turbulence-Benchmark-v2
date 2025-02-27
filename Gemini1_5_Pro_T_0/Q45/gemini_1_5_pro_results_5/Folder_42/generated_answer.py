import itertools

def palindromes_between_indices(string):
    letters = []
    for i in range(6, 10):
        if 0 <= i < len(string) and string[i].isalpha():
            letters.append(string[i].lower())
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes