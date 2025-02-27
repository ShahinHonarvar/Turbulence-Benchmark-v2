import itertools

def palindromes_between_indices(string):
    s = string[3:10].lower()
    letters = [l for l in s if l.isalpha()]
    result = set()
    if len(letters) >= 7:
        for i in range(7, len(letters) + 1):
            for p in itertools.permutations(letters, i):
                word = ''.join(p)
                if word == word[::-1]:
                    result.add(word)
    return result