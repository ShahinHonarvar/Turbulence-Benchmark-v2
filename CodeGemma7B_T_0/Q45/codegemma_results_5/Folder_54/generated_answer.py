import re
    import itertools

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    if len(text) < 10:
        return set()
    letters = text[4:10]
    if not letters:
        return set()
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if palindrome in palindromes:
            continue
        if palindrome not in palindromes and len(palindrome) >= 4:
            palindromes.add(palindrome)
    return palindromes