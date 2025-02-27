import itertools

def palindromes_between_indices(string):
    letters = []
    for i in range(1, 7):
        if ord(string[i]) >= 97 and ord(string[i]) <= 122 or (ord(string[i]) >= 65 and ord(string[i]) <= 90):
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in itertools.permutations(letters, i):
            word = ''.join(j)
            if len(word) >= 7 and word == word[::-1]:
                result.add(word)
    return result