import re
    import itertools

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    letters = text[1:7]
    if not letters:
        return set()
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes