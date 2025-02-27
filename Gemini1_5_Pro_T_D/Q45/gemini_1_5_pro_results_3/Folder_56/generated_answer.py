from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(5, 10):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    for i in range(5, len(letters) + 1):
        for item in permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1] and word not in result:
                result.add(word)
    return result