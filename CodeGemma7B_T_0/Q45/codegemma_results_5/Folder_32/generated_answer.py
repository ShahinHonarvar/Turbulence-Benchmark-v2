import re
    from itertools import permutations

def palindromes_between_indices(text):
    text = re.sub('[^\\\\w]', '', text).lower()
    letters = text[1:8]
    if len(letters) < 5:
        return set()
    palindromes = set()
    for p in permutations(letters):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes