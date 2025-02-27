import re
    from itertools import permutations

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text)
    text = text.lower()
    if len(text) < 5:
        return set()
    palindromes = set()
    for i in range(len(text) - 3):
        for j in range(i + 4, len(text) + 1):
            word = ''.join((p for p in permutations(text[i:j])))
            if word in palindromes:
                continue
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes