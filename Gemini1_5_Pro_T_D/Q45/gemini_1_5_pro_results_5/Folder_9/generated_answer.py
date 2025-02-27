import itertools

def palindromes_between_indices(string):
    letters = set([char.lower() for char in string[:7] if char.isalpha()])
    palindromes = set()
    for i in range(7, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1] and len(word) >= 7:
                palindromes.add(word)
    return palindromes