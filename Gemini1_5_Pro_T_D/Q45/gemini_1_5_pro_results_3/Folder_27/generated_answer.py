from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    s = text[2:9].lower()
    chars = []
    for c in s:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            chars.append(c)
    for i in range(6, len(chars) + 1):
        for p in permutations(chars, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result