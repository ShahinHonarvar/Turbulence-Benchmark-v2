from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = set([char.lower() for char in string[:5] if char.isalpha()])
    result = set()
    for i in range(4, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if word == word[::-1] and word not in result:
                result.add(word)
    return result