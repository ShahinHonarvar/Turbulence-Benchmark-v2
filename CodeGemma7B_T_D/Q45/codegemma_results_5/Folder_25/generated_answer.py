import itertools
import re

def palindromes_between_indices(text):
    seen = set()
    for indices in itertools.combinations(range(1, 5), 2):
        first, second = indices
        word = text[first:second + 1].lower()
        if re.fullmatch('[a-z]{3,}', word):
            seen.add(''.join(sorted(word)))
    return seen