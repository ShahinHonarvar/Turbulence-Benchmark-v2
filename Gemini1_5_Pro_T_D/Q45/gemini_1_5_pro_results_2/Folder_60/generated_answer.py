import itertools

def palindromes_between_indices(string):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    chars = []
    for i in range(3, 7):
        if string[i].lower() in english_letters:
            chars.append(string[i].lower())
    result = set()
    for i in range(4, len(chars) + 1):
        for item in itertools.permutations(chars, i):
            word = ''.join(item)
            if word == word[::-1] and len(word) >= 4:
                result.add(word)
    return result