import re

def palindromes_of_specific_lengths(str1):
    result = set()
    pattern = re.compile('[a-zA-Z]{23,36}')
    for i in range(18, 66):
        for j in range(i, 66):
            substring = str1[i:j + 1]
            if pattern.match(substring):
                result.add(substring)
    return result