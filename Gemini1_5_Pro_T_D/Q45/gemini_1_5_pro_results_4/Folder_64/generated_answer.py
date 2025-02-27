import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(re.findall('[a-zA-Z]+', string[4:10]))
    s = set()
    if len(letters) >= 5:
        for i in range(5, len(letters) + 1):
            for p in permutations(letters.lower(), i):
                candidate = ''.join(p)
                if candidate == candidate[::-1]:
                    s.add(candidate)
    return s