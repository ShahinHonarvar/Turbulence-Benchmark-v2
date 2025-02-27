from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string: str) -> set[str]:
    letters = []
    for i in range(6):
        if i < len(string) and string[i].isalpha():
            letters.append(string[i].lower())
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for permutation in permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes