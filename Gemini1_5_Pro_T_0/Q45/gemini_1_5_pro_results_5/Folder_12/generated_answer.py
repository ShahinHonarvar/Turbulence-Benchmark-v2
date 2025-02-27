from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[3:9]
    for i in range(4, len(s) + 1):
        for p in permutations(s, i):
            temp = ''.join(p)
            if temp.lower() == temp[::-1].lower():
                result.add(temp.lower())
    return result