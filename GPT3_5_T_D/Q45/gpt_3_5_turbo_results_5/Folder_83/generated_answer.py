import itertools
    import re

def palindromes_between_indices(string):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    letters = re.findall('[a-zA-Z]', string[2:10])
    if len(letters) < 7:
        return set()
    palindromes = set()
    for p in itertools.permutations(letters):
        word = ''.join(p)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes