import re
  from itertools import permutations

def palindromes_between_indices(string):
    s = ''.join(sorted(set(re.sub('[^a-zA-Z]+', '', string[3:9]).lower())))
    palindromes = set()
    if len(s) >= 5:
        for i in range(5, len(s) + 1):
            for p in permutations(s, i):
                word = ''.join(p)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes