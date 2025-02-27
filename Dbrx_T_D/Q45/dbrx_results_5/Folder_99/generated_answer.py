from itertools import permutations

def generate_palindromes(string, index1, index2):
    candidates = set()
    for i in range(index1, index2 + 1):
        for j in range(i, index2 + 1):
            candidate = string[i:j + 1].lower()
            if candidate[0] != ' ' and candidate[0].isalpha() and (len(candidate) >= 3) and (candidate == candidate[::-1]):
                candidates.add(candidate)
    return candidates

def palindromes_between_indices(string):
    return generate_palindromes(string, 4, 8)