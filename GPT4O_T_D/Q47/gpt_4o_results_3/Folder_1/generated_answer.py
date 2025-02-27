import re

def palindromes_of_specific_lengths(s):
    s = re.sub('[^a-zA-Z]', '', s[15:90]).lower()
    palindromes = set()
    n = len(s)
    for length in range(40, 73):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes