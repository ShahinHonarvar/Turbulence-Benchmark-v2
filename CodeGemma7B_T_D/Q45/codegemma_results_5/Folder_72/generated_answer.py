from itertools import permutations
  from string import ascii_lowercase

def palindromes_between_indices(string):
    if not string[1:7].lower().isalpha():
        return set()
    low, high = (set(), set())
    for i in permutations(string[1:7].lower()):
        low.add(''.join(i))
    for i in permutations(string[1:7].lower(), r=6):
        high.add(''.join(i))
    return low.intersection(high)