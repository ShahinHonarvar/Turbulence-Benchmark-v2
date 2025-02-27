import re
    from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(re.findall('[a-zA-Z]', string[5:8]))
    result = set()
    if len(letters) < 3:
        return result
    for i in range(3, len(letters) + 1):
        for item in permutations(letters.lower(), i):
            word = ''.join(item)
            if word == word[::-1]:
                result.add(word)
    return result