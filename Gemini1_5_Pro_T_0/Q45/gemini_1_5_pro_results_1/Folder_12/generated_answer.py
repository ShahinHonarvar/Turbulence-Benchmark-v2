from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for i in range(3, 9):
        for j in permutations(string[3:9], i):
            temp = ''.join(j)
            if len(temp) >= 4 and temp.lower() == temp[::-1].lower():
                result.add(temp.lower())
    return result