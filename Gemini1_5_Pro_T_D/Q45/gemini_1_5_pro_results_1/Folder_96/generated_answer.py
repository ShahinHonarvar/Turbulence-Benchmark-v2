import itertools

def palindromes_between_indices(string):
    s = string[3:9].lower()
    letters = [l for l in s if l.isalpha()]
    result = set()
    if len(letters) >= 6:
        for i in range(6, len(letters) + 1):
            for item in itertools.permutations(letters, i):
                word = ''.join(item)
                if word == word[::-1]:
                    result.add(word)
    return result