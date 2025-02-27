import re

def palindromes_of_specific_lengths(s):
    s = re.sub('[^a-zA-Z]', '', s[3:301]).lower()
    palindromes = set()
    length = len(s)
    for size in range(30, 301):
        for i in range(length - size + 1):
            substring = s[i:i + size]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes