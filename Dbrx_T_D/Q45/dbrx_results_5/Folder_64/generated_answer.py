import re
    from collections import Set

def palindromes_between_indices(s):
    s = re.sub('[^a-zA-Z]', '', s).lower()
    substring = s[4:10]
    palindromes = set()
    for i in range(5, len(substring) + 1):
        for j in range(len(substring) - i + 1):
            if substring[j:j + i] == substring[j:j + i][::-1]:
                palindromes.add(substring[j:j + i])
    return palindromes