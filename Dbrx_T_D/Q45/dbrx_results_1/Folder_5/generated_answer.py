import re

def palindromes_between_indices(s):
    s = s.lower()
    letters = re.findall('[a-z]', s[4:9])
    palindromes = {word for word in {''.join(letter_combination) for letter_combination in itertools.combinations(letters, 4)} if word == word[::-1]}
    return palindromes