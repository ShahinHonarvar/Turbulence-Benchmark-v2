import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = re.findall('[a-zA-Z]', s)
    for i in range(0, 7):
        for j in range(3, 7):
            if i + j <= 7:
                substring = s[i:i + j]
                if substring == substring[::-1]:
                    palindromes.add(''.join(substring).lower())
    return palindromes