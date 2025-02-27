import re

def palindromes_between_indices(s):
    corrected = re.sub('[^A-Za-z]', '', s[6:9])
    output = set()
    for i in range(4, len(corrected) + 1):
        for j in itertools.permutations(corrected, i):
            output.add(''.join(j))
    return output