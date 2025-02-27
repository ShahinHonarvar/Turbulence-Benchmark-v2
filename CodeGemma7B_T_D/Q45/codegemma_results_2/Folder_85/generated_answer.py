import re

def palindromes_between_indices(string):

    def is_palindrome(word):
        return word == word[::-1]
    lowered_string = string.lower()
    letters = re.findall('[a-z]', lowered_string)[2:9]
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if is_palindrome(palindrome) and len(palindrome) >= 7:
            palindromes.add(palindrome)
    return palindromes