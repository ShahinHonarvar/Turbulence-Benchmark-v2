from itertools import combinations

def palindrome_of_length_at_least_n(text):
    """
    Takes one argument, a string, and returns the set of all palindromes of the length greater than or equal to 86 that exist in the given string. Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """

    def is_palindrome(word):
        return word == word[::-1]
    result = set()
    for length in range(86, len(text) + 1):
        for start in range(len(text) - length + 1):
            word = text[start:start + length]
            if is_palindrome(word):
                result.add(word.lower())
    return result