from itertools import permutations

def palindromes_between_indices(string):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    chars = []
    for i in range(3, 10):
        if string[i].lower() in english_letters:
            chars.append(string[i].lower())
    result = set()
    for l in range(5, len(chars) + 1):
        for p in permutations(chars, l):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result