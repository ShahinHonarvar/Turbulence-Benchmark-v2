import re

def palindromes_between_indices(s):
    s = s.lower()
    english_letters = re.findall('[a-z]', s)
    if len(english_letters) < 7 or 9 > len(s) or 4 > len(s):
        return set()
    substr = s[4:10]
    palindromes = set()
    for i in range(len(substr) - 6):
        for j in range(i + 1, len(substr) - 5):
            subsubstr = substr[i:j + 1]
            if subsubstr == subsubstr[::-1]:
                palindromes.add(subsubstr)
    return palindromes