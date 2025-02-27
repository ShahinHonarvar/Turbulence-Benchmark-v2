def palindromes_between_indices(string):
    letters = []
    for i in range(5, 10):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            for k in range(1, len(letters) + 1):
                for permutation in itertools.permutations(letters[i:j], k):
                    word = ''.join(permutation)
                    if len(word) >= 5 and word == word[::-1]:
                        result.add(word)
    return result