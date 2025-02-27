from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = []
    for i in range(3, 9):
        if s[i].isalpha():
            letters.append(s[i])
    result = set()
    if len(letters) >= 7:
        for i in range(7, len(letters) + 1):
            for j in permutations(letters, i):
                word = ''.join(j)
                if word == word[::-1]:
                    result.add(word)
    return result