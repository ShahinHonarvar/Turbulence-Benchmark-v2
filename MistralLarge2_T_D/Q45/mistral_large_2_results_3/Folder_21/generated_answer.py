import re
    from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:9].lower()
    english_letters = re.findall('[a-z]', substring)
    palindromes = set()
    for length in range(7, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes