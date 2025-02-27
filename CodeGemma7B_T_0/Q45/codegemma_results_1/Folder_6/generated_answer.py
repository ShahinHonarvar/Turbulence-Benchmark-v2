import re
    import itertools

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    if len(text) < 4:
        return set()
    letters = text[0:8]
    if not letters:
        return set()
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if palindrome in palindromes:
            continue
        if palindrome not in text:
            continue
        if len(palindrome) < 4:
            continue
        palindromes.add(palindrome)
    return palindromes