import re
    from itertools import permutations

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    if len(text) < 7:
        return set()
    letters = text[0:7]
    palindromes = set()
    for p in permutations(letters):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes