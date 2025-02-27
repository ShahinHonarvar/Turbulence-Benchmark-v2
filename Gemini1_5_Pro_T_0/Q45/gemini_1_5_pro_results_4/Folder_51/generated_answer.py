import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(set(re.sub('[^a-zA-Z]+', '', string[3:6]).lower())))
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            s = ''.join(p)
            if s == s[::-1]:
                palindromes.add(s)
    return palindromes