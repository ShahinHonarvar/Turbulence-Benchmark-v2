from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    chars = []
    for i in range(3, 10):
        if i <= len(string) - 1 and string[i].isalpha() and (len(string[i]) == 1):
            chars.append(string[i].lower())
    for l in range(7, len(chars) + 1):
        for p in permutations(chars, l):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result