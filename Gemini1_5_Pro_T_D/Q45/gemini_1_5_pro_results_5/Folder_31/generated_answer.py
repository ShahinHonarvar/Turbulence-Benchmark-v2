from itertools import permutations

def palindromes_between_indices(string):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    chars = []
    for i in range(1, 9):
        if string[i].lower() in english_letters:
            chars.append(string[i].lower())
    result = set()
    for i in range(6, len(chars) + 1):
        for item in permutations(chars, i):
            word = ''.join(item)
            if word == word[::-1]:
                result.add(word)
    return result