def palindromes_between_indices(string):
    letters = set(string[0:5].lower())
    result = set()
    if len(letters) < 3 or not letters.issubset(set('abcdefghijklmnopqrstuvwxyz')):
        return result
    for i in range(4):
        for j in range(i + 1, 5):
            word = ''.join(sorted(letters[i:j + 1]))
            result.add(word)
    return result