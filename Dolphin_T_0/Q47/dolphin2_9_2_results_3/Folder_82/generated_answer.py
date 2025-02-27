import re

def palindromes_of_specific_lengths(s):
    s = s[2:301]
    palindromes = set()
    for i in range(30, 301):
        for j in range(0, len(s) - i + 1):
            if re.match('^[a-zA-Z]{' + str(i) + '}$', s[j:j + i]) and s[j:j + i].lower() == s[j:j + i].lower()[::-1]:
                palindromes.add(s[j:j + i])
    return palindromes