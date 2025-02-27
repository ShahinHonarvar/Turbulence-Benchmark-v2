from itertools import permutations

def palindromes_between_indices(s):
    result = set()
    for i in range(1, 6):
        temp = []
        for j in permutations(s[1:6]):
            if j not in temp and j.lower() > result:
                temp.append(j)
        result |= {''.join(i) for i in temp}
    return result