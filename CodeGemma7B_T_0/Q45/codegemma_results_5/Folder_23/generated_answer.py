import re
    import itertools

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    letters = text[0:7]
    palindromes = set()
    for permutation in itertools.permutations(letters):
        if len(permutation) >= 4 and permutation == permutation[::-1]:
            palindromes.add(''.join(permutation))
    return palindromes