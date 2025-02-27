import itertools

def palindromes_between_indices(text):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    chars = []
    for i in range(2, 6):
        if text[i].lower() in english_letters:
            chars.append(text[i].lower())
    result = set()
    for length in range(4, len(chars) + 1):
        for item in itertools.permutations(chars, length):
            word = ''.join(item)
            if word == word[::-1]:
                result.add(word)
    return result