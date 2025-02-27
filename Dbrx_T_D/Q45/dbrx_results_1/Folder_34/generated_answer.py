import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[5:8])
    palindromes = {word for word in {''.join(p) for p in itertools.product(letters, repeat=4)} if word == word[::-1]}
    return palindromes