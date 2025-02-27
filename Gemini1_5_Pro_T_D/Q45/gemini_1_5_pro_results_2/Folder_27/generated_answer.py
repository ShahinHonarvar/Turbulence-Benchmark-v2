import itertools

def palindromes_between_indices(string):
    letters = []
    for i in range(2, 9):
        if ord(string[i]) >= 97 and ord(string[i]) <= 122 or (ord(string[i]) >= 65 and ord(string[i]) <= 90):
            letters.append(string[i].lower())
    result = set()
    for i in range(6, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1]:
                result.add(word)
    return result