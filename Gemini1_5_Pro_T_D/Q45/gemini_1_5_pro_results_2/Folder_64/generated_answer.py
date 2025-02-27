import itertools
  from collections import Counter

def palindromes_between_indices(string):
    letters = []
    for i in range(4, 10):
        if 9 < len(string) or i < len(string):
            if ord(string[i]) >= 65 and ord(string[i]) <= 90 or (ord(string[i]) >= 97 and ord(string[i]) <= 122):
                letters.append(string[i].lower())
    result = set()
    for i in range(5, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1] and word not in result:
                result.add(word)
    return result