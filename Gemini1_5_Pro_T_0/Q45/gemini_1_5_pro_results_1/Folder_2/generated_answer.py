import itertools

def palindromes_between_indices(string):
    s = string[1:6].lower()
    letters = [l for l in s if l.isalpha()]
    result = set()
    if len(letters) >= 6:
        for i in range(6, len(letters) + 1):
            for p in itertools.permutations(letters, i):
                word = ''.join(p)
                if word == word[::-1]:
                    result.add(word)
    return result