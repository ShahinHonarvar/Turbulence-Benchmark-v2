from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[1:5]
    for i in range(3, len(s) + 1):
        for p in permutations(s, i):
            temp = ''.join(p).lower()
            if temp == temp[::-1]:
                result.add(temp)
    return result