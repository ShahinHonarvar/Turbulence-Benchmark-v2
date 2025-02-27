import re
  from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter(re.findall('[a-zA-Z]', string[2:8]))
    palindromes = set()
    for perm in {''.join(p) for i in range(1, len(letters) + 1) for p in permutations(letters, i)}:
        word = ''.join(perm)
        if len(word) >= 6 and word == word[::-1]:
            if all((letters[c] >= word.lower().count(c) for c in set(word.lower()))):
                palindromes.add(word)
    return palindromes