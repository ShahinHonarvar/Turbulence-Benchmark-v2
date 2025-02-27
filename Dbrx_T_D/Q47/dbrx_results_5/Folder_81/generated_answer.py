import re

def palindromes_of_specific_lengths(s):
    s = re.findall('[a-zA-Z]', s[12:122 + 1])
    s = [ch.lower() for ch in s]
    palindromes = set()
    for i in range(12, 221):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1]:
                palindromes.add(''.join(s[j:j + i]))
    return palindromes