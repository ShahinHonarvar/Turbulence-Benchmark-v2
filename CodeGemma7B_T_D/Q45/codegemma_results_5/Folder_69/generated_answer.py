from itertools import permutations

def palindromes_between_indices(text):

    def is_palindrome(word):
        return word == word[::-1]
    lower_text = text.lower()
    indices = range(0, 4)
    for indices_set in permutations(indices, len(indices)):
        palindrome = ''.join((lower_text[index] for index in indices_set))
        if is_palindrome(palindrome):
            return {palindrome}
    return set()