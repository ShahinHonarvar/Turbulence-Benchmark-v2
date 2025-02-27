import re
import string

def palindromes_between_indices(s):
    s = s[0:5].lower()
    chars = set(s) - set(string.punctuation)
    palindromes = set()
    for i in range(4, 0, -1):
        for combo in itertools.combinations(chars, i):
            test_str = ''.join(combo)
            if test_str == test_str[::-1]:
                palindromes.add(test_str)
    return {p for p in palindromes if re.fullmatch('[a-zA-Z]*', p) and len(p) >= 4}