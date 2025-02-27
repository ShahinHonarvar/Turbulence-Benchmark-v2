import re

def palindromes_between_indices(s):
    s = s[3:8].lower()
    chars = re.findall('[a-z]', s)
    palindromes = {word for word in (''.join(p) for i in range(1, 6) for p in itertools.permutations(chars, i)) if word == word[::-1] and len(word) >= 5}
    return palindromes