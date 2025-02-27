import re
    import itertools

def palindromes_between_indices(text):
    if not re.search('[a-zA-Z]', text[3:6]):
        return set()
    letters = re.findall('[a-zA-Z]', text[3:6])
    return {''.join(p) for p in itertools.permutations(letters)}