from itertools import permutations

def palindromes_between_indices(string):
    s = set()
    for p in permutations(string[1:4]):
        temp = ''.join(p)
        if len(temp) >= 4 and temp.lower() == temp[::-1].lower():
            s.add(temp.lower())
    return s