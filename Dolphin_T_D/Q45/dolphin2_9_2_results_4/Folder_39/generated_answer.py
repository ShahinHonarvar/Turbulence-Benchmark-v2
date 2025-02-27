import re

def palindromes_between_indices(s):
    letters = re.sub('[^a-zA-Z]', '', s[2:6]).lower()
    result = set()
    for i in range(3, len(letters) + 1):
        if re.search('^(([a-z])(?=.*\\2))*$', letters[i - 1:]):
            result.add(letters[i - 1])
    return result