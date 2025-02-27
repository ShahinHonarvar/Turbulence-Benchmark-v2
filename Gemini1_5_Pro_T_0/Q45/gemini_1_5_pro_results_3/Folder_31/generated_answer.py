import re
  from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter(re.findall('[a-zA-Z]', string[1:9]))
    palindromes = set()
    for perm in {''.join(p) for i in range(3, len(letters) + 1) for p in permutations(letters.elements(), i)}:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes