from itertools import permutations
  import string

def palindromes_between_indices(s):
    result = set()
    for x in permutations(s[3:6]):
        temp = ''.join(x)
        result.add(temp)
    return result