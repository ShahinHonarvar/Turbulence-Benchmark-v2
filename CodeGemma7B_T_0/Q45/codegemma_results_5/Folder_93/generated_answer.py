import re
  from itertools import permutations

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text)
    text = text.lower()
    if len(text) < 6:
        return set()
    text = text[2:8]
    palindromes = set()
    for permutation in permutations(text):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes