def palindromes_between_indices(string):
    letters = []
    for i in range(0, 8):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(0, len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    temp = [letters[i], letters[j], letters[k], letters[l]]
                    for permutation in permutations(temp):
                        word = ''.join(permutation)
                        if word == word[::-1] and len(word) >= 4:
                            result.add(word)
    return result

def permutations(s):
    if len(s) <= 1:
        yield s
    else:
        for i, x in enumerate(s):
            for p in permutations(s[:i] + s[i + 1:]):
                yield ([x] + p)