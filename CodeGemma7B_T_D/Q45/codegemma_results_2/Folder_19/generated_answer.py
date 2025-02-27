from itertools import permutations

def palindromes_between_indices(text):
    """
    Returns a set of palindromes of the length of at least 7 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 1 to index 7, both inclusive.
    """
    set_of_letters = set(text.lower())
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    if english_letters.issubset(set_of_letters) and text[0] <= 'z' and (text[-1] >= 'a'):
        for i in range(7, len(text)):
            for p in permutations(text[1:i + 1]):
                if ''.join(p * 2) == text[0:i + 1]:
                    return {''.join(p * 2)}
    return set()