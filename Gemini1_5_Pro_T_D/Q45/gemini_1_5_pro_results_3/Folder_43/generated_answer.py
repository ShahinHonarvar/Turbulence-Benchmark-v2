from itertools import permutations

def palindromes_between_indices(text):
    letters = []
    for i in range(2, 6):
        if text[i].isalpha():
            letters.append(text[i].lower())
    result = set()
    for i in range(4, len(letters) + 1):
        for item in permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1] and len(word) >= 4:
                result.add(word)
    return result