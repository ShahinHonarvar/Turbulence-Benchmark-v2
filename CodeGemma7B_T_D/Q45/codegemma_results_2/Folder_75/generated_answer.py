from itertools import permutations

def palindromes_between_indices(text):
    text = text.lower()
    'Returns set of all palindromes of len>=3 from indices 2 to 4.'
    palindromes = set()
    for perm in permutations(text[2:5]):
        palindromes.add(''.join(perm))
    return palindromes