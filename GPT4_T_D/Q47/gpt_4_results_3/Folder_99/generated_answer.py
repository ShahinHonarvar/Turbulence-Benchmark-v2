import re

def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for i in range(127, 289):
        for j in range(i + 119, min(i + 142, 289)):
            temp = re.sub('[^a-z]', '', s[i:j])
            if temp == temp[::-1]:
                result.add(temp)
    return result