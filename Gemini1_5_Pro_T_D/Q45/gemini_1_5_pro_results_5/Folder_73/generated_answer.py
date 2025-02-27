from itertools import permutations

def palindromes_between_indices(string):
    s = string[3:7].lower()
    letters = []
    for char in s:
        if ord(char) >= 97 and ord(char) <= 122:
            letters.append(char)
    pals = set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1] and word not in pals:
                pals.add(word)
    return pals