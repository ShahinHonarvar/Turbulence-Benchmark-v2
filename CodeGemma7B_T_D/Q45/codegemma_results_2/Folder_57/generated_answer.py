from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    for i in permutations(text[2:5]):
        temp = ''.join(i)
        if temp == temp[::-1] and len(temp) >= 5:
            result.add(temp.lower())
    return result