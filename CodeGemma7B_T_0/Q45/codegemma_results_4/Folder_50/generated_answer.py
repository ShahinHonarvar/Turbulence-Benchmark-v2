import re
    import itertools

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    text = text[4:9]
    if len(text) < 5:
        return set()
    letters = set(text)
    if len(letters) < 5:
        return set()
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if palindrome in text:
            palindromes.add(palindrome)
    return palindromes