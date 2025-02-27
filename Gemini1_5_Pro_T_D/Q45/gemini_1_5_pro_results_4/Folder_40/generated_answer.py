import itertools

def palindromes_between_indices(string):
    letters = []
    for i in range(4, 10):
        if string[i].isalpha() and string[i].lower() not in letters:
            letters.append(string[i].lower())
    result = set()
    for i in range(7, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1] and word not in result:
                result.add(word)
    return result