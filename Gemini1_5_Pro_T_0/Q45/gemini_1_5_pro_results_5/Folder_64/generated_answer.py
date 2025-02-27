import itertools

def palindromes_between_indices(string):
    s = string[4:10].lower()
    letters = [ch for ch in s if ch.isalpha()]
    result = set()
    if len(letters) >= 5:
        for i in range(5, len(letters) + 1):
            for item in itertools.permutations(letters, i):
                word = ''.join(item)
                if word == word[::-1]:
                    result.add(word)
    return result