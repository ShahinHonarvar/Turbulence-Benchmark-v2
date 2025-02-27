import re
    from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(sorted(re.findall('[a-zA-Z]', text[5:8])))
    if len(letters) < 4:
        return set()
    result = set()
    for i in range(4, len(letters) + 1):
        for x in permutations(letters, i):
            s = ''.join(x)
            if s == s[::-1]:
                result.add(s)
    return result