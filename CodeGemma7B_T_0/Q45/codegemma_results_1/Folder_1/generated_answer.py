import re
    from itertools import permutations

def palindromes_between_indices(text):

    def is_palindrome(word):
        return word == word[::-1]
    text = re.sub('[^a-zA-Z]', '', text).lower()
    letters = text[4:8]
    if not letters:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        palindrome = ''.join(perm)
        if is_palindrome(palindrome):
            palindromes.add(palindrome)
    return palindromes