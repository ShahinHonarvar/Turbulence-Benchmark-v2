from collections import Counter

def palindromes_between_indices(string):
    letters = set(string[0:3].lower()) & set('abcdefghijklmnopqrstuvwxyz')
    counts = Counter((c.lower() for c in string if c.lower() in letters))
    result = set()
    if len(letters) < 3:
        return result
    for i in letters:
        for j in letters:
            for k in letters:
                word = i + j + k
                if word[::-1] == word and (i != j or j != k):
                    test = Counter((c for c in word))
                    possible = True
                    for c in test:
                        if counts[c] < test[c]:
                            possible = False
                    if possible:
                        result.add(word)
    return result