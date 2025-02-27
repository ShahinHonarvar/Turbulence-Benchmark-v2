import itertools

def palindromes_between_indices(string):
    letters = []
    for i in range(4, 10):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    for i in range(6, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1]:
                result.add(word)
    return result