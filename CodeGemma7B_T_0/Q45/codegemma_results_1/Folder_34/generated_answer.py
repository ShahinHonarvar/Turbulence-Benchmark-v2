import re
    import itertools

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text)
    text = text.lower()
    if len(text) < 4 or not text[5:8]:
        return set()
    letters = list(set(text[5:8]))
    if len(letters) < 2:
        return set()
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if palindrome in text[5:8]:
            palindromes.add(palindrome)
    return palindromes