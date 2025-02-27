import re

def palindromes_between_indices(s):
    s = s.lower()
    letters = re.findall('[a-z]', s[4:9])
    palindromes = {word for word in {''.join(letter) for length in range(3, 6) for letter in itertools.combinations_with_replacement(letters, length)} if word == word[::-1]}
    return palindromes