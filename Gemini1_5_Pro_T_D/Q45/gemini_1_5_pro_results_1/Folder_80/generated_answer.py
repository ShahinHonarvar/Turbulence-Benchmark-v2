import itertools

def palindromes_between_indices(string):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    chars = []
    for i in range(3, 9):
        if string[i].lower() in english_letters:
            chars.append(string[i].lower())
    result = set()
    for i in range(7, len(chars) + 1):
        for item in itertools.permutations(chars, i):
            candidate = ''.join(item)
            if candidate == candidate[::-1] and len(candidate) >= 7:
                result.add(candidate)
    return result