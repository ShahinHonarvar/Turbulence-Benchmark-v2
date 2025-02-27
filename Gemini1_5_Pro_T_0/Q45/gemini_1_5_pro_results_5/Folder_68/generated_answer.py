from collections import Counter
  from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(sorted((c for c in text[1:9] if c.isalpha()))).lower()
    result = set()
    for i in range(4, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                if all((Counter(word)[l] <= Counter(letters)[l] for l in word)):
                    result.add(word)
    return result