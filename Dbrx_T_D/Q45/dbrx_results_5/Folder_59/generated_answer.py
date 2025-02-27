import re

def palindromes_between_indices(s):
    english_letters = re.findall('[a-zA-Z]', s[8:10])
    if len(english_letters) < 3:
        return set()
    palindromes = {word for word in {''.join(p) for p in itertools.product(english_letters, repeat=len(english_letters))} if word == word[::-1]}
    return palindromes