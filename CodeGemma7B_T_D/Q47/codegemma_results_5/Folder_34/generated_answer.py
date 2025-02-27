import re

def palindromes_of_specific_lengths(s):
    result = set()
    pattern = re.compile('[a-zA-Z]{10,50}')
    for i in range(200, 300 + 1):
        for j in range(i, 300 + 1):
            substring = s[i:j + 1]
            for m in pattern.finditer(substring):
                palindrome = m.group(0)
                if palindrome.lower() in result:
                    continue
                result.add(palindrome.lower())
    return result