import re

def palindromes_between_indices(s):
    s = s.lower()
    letters = re.findall('[a-z]', s[5:9])
    palindromes = {pal for length in range(3, len(letters) + 1) for pal in set(permutations(letters, length)) if pal == pal[::-1]}
    return palindromes