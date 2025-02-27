import itertools

def palindromes_between_indices(string):
    s = string[3:8].lower()
    letters = []
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            letters.append(c)
    result = set()
    for i in range(5, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1]:
                result.add(word)
    return result