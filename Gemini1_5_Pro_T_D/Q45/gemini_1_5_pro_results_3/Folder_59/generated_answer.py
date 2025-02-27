import re

def palindromes_between_indices(string):
    letters = sorted(set(re.findall('[a-zA-Z]', string[8:10])))
    if len(letters) < 3:
        return set()
    result = set()
    for i in range(len(letters)):
        for j in range(len(letters)):
            for k in range(len(letters)):
                word = letters[i] + letters[j] + letters[k]
                if word.lower() == word[::-1].lower():
                    result.add(word.lower())
    return result