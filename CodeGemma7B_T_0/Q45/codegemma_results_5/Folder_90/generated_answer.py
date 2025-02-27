import re
    import itertools

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    if len(text) < 5:
        return set()
    letters = list(text[0:6])
    if not letters:
        return set()
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1] and len(palindrome) >= 4:
            palindromes.add(palindrome)
    return palindromes