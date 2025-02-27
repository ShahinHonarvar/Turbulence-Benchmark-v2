import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[7:9])
    palindromes = {word for word in {''.join(pal) for pal in itertools.product(letters, repeat=len(letters))} if len(word) >= 3 and word == word[::-1]}
    return palindromes