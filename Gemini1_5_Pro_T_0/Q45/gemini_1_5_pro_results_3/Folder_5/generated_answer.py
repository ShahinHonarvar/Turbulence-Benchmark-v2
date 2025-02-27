from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(4, 9):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            for k in range(len(substring) + 1):
                for permutation in permutations(substring[:k], k):
                    for l in range(len(substring) + 1):
                        for permutation2 in permutations(substring[l:], len(substring) - l):
                            candidate = ''.join(permutation) + ''.join(permutation2)
                            if len(candidate) >= 4 and candidate == candidate[::-1]:
                                result.add(candidate)
    return result