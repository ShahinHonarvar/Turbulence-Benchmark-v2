from itertools import permutations
    import re

def palindromes_between_indices(text):
    """
    This function takes one argument, which is a string.
    The given string may consist of any character.
    The function should return the set of all palindromes of the length of at least 3 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 1 to index 2, both inclusive.
    If no such palindromes of the specified length can be created from the English letters of the given string that occur in the specified range, the function should return an empty set.
    The function should form each palindrome in a case-insensitive manner.
    """

    def is_palindrome(text):
        return text == text[::-1]

    def get_english_letters(text):
        return re.findall('[a-zA-Z]', text)

    def get_palindromes(text):
        english_letters = get_english_letters(text)
        if not english_letters:
            return set()
        palindromes = set()
        for i in range(len(english_letters)):
            for j in range(i + 1, len(english_letters)):
                for k in range(j + 1, len(english_letters)):
                    for p in permutations(english_letters[i:k + 1]):
                        palindromes.add(''.join(p))
        return palindromes

    def get_palindromes_between_indices(text, start_index, end_index):
        if not text or start_index < 1 or end_index > len(text) or (start_index > end_index):
            return set()
        return get_palindromes(text[start_index - 1:end_index])
    return get_palindromes_between_indices(text, 1, 2)