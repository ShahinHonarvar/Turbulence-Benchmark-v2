from itertools import permutations

def palindromes_between_indices(string):
    palindromes = set()
    for i in range(0, 6):
        for j in range(i + 1, 6):
            word = ''.join((p for p in permutations(string[i:j + 1], r=j - i + 1)))
            if word == word[::-1] and word.lower() not in palindromes:
                palindromes.add(word.lower())
    return palindromes