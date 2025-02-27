import re
    from itertools import permutations

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text)
    text = text.lower()
    text = text[4:10]
    if not text:
        return set()
    palindromes = set()
    for p in permutations(text):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes