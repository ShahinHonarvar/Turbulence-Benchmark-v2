import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(re.findall('[a-zA-Z]+', string[5:8]))
    output = set()
    if len(letters) >= 3:
        for i in range(3, len(letters) + 1):
            for p in permutations(letters.lower(), i):
                if ''.join(p) == ''.join(p)[::-1]:
                    output.add(''.join(p))
    return output