import re

def palindromes_between_indices(s):
    s = s.lower()
    letters = set(re.findall('[a-z]', s[:7]))
    palindromes = {word for word in letters for i in range(3, 7) if word * i == word[i:] + word[:i]}
    return palindromes