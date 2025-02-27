from itertools import permutations

def palindromes_between_indices(text):
    """
    Returns a set of all palindromes of the length of at least 3 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 2 to index 7, both inclusive.
    """
    if not text or len(text) < 6:
        return set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    relevant_letters = [letter for letter in text[2:8].lower() if letter in english_letters]
    if not relevant_letters:
        return set()
    palindromes = set()
    for permutation in permutations(relevant_letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 3:
            palindromes.add(palindrome)
    return palindromes