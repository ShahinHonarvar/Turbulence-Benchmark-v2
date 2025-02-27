from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    s = text[4:10].lower()
    for i in range(4, len(s) + 1):
        for p in permutations(s, i):
            word = ''.join(p)
            if word == word[::-1] and word.isalpha():
                result.add(word)
    return result