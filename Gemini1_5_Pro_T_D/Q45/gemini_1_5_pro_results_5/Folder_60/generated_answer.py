import itertools

def palindromes_between_indices(string):
    s = string[3:7].lower()
    letters = [c for c in s if c.isalpha()]
    result = set()
    for i in range(4, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1] and len(word) >= 4:
                result.add(word)
    return result