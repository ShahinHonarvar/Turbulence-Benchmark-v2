from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:8])).lower()
    result = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                result.add(word)
    return result