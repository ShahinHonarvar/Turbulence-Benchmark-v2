import re
  from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(re.sub('[^a-zA-Z]+', '', string[1:8]).lower()))
    result = set()
    for i in range(3, len(letters) + 1):
        for p in [''.join(p) for p in permutations(letters, i)]:
            if p == p[::-1] and p not in result:
                result.add(p)
    return result