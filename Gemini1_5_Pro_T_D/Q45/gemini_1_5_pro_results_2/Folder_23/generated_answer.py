from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(7):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for s in permutations(letters, len(letters)):
        candidate = ''.join(s)
        if len(candidate) >= 4 and candidate == candidate[::-1]:
            result.add(candidate)
    return result