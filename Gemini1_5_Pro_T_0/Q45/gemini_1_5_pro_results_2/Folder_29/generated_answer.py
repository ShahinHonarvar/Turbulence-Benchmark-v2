import itertools

def palindromes_between_indices(string):
    letters = []
    for i in range(2, 10):
        if i < len(string) and ord('a') <= ord(string[i].lower()) <= ord('z'):
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for permutation in itertools.permutations(letters, i):
            word = ''.join(permutation)
            if len(word) >= 6 and word == word[::-1]:
                result.add(word)
    return result