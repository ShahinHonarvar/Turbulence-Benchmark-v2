import itertools

def palindromes_between_indices(string):
    letters = []
    for i in range(2, 10):
        if i < len(string) and ord('a') <= ord(string[i].lower()) <= ord('z'):
            letters.append(string[i].lower())
    result = set()
    for i in range(4, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            current = ''.join(item)
            if current == current[::-1]:
                result.add(current)
    return result