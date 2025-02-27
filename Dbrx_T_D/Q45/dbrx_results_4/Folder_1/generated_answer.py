import re
    from collections import Set

def palindromes_between_indices(s):
    substring = s[4:8].lower()
    palindromes = set()
    for i in range(5, len(substring) + 1):
        for j in range(len(substring) - i + 1):
            candidate = substring[j:j + i]
            if candidate == candidate[::-1] and re.fullmatch('[a-z]*', candidate):
                palindromes.add(candidate)
    return palindromes