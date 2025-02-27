from itertools import permutations

def palindromes_between_indices(string):
    s = string[3:8].lower()
    letters = [l for l in s if l.isalpha()]
    output = set()
    if len(letters) >= 6:
        for i in range(6, len(letters) + 1):
            for p in permutations(letters, i):
                word = ''.join(p)
                if word == word[::-1]:
                    output.add(word)
    return output