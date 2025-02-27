import re
    from itertools import permutations

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    if len(text) < 4:
        return set()
    palindromes = set()
    for i in range(len(text) - 3):
        for j in range(i + 1, len(text) - 2):
            for k in range(j + 1, len(text) - 1):
                for l in range(k + 1, len(text)):
                    word = ''.join(permutations(text[i:l + 1]))
                    if word == word[::-1] and len(word) >= 4:
                        palindromes.add(word)
    return palindromes