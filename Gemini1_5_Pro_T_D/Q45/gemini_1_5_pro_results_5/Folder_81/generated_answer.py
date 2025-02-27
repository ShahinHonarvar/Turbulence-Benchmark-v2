import itertools

def palindromes_between_indices(string):
    letters = set()
    for i in range(0, 7):
        if string[i].isalpha():
            letters.add(string[i].lower())
    result = set()
    for i in range(3, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            candidate = ''.join(item)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result