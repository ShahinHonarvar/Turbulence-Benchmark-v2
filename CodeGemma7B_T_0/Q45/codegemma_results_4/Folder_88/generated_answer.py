import re
    import itertools

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    if len(text) < 6 or not text[3:8]:
        return set()
    letters = list(text[3:8])
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes