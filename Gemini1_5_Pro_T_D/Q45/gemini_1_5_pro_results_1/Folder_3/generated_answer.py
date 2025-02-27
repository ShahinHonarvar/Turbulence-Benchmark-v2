import re

def palindromes_between_indices(string):
    letters = sorted(set(re.findall('[a-zA-Z]', string[7:10])), key=str.casefold)
    if len(letters) < 3:
        return set()
    result = set()

    def helper(current):
        if len(current) == len(letters):
            word = ''.join(current)
            if word == word[::-1]:
                result.add(word)
            return
        for i in range(len(letters)):
            if i not in current:
                helper(current + [i])
    helper([])
    return {''.join([letters[i] for i in list(perm)]) for perm in result}