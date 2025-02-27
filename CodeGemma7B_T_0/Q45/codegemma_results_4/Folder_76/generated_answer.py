from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(text):
    """
    This function takes a string as an argument and returns the set of all palindromes of the length of at least 4 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 1 to index 4, both inclusive. If no such palindromes of the specified length can be created from the English letters of the given string that occur in the specified range, the function should return an empty set. The function should form each palindrome in a case-insensitive manner.
    """
    text = text.lower()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for i in range(len(text) - 3):
        for j in range(i + 4, len(text) + 1):
            for letters in permutations(text[i:j]):
                word = ''.join(letters)
                if is_palindrome(word):
                    palindromes.add(word)
    return palindromes