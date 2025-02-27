import itertools

def palindromes_between_indices(text):
    letters = set()
    for i in range(2, min(len(text), 10)):
        if text[i].isalpha():
            letters.add(text[i].lower())
    result = set()
    for i in range(4, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1]:
                result.add(word)
    return result