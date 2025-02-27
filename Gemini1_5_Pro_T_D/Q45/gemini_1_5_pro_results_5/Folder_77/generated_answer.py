import itertools

def palindromes_between_indices(string):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    letters = []
    for i in range(4, 7):
        if string[i].lower() in english_letters:
            letters.append(string[i].lower())
    result = set()
    if len(letters) >= 4:
        for i in range(4, len(letters) + 1):
            for j in itertools.permutations(letters, i):
                word = ''.join(j)
                if word == word[::-1] and word not in result:
                    result.add(word)
    return result