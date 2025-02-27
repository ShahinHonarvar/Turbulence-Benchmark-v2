from itertools import permutations

def palindromes_between_indices(text: str) -> set:
    """
    The function takes one argument, which is a string.
    The given string may consist of any character.
    The function should return the set of all palindromes of the length of at least 4 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 1 to index 5, both inclusive.
    If no such palindromes of the specified length can be created from the English letters of the given string that occur in the specified range, the function should return an empty set.
    The function should form each palindrome in a case-insensitive manner.
    """
    combinations = permutations(text[1:6].lower(), 5)
    palindromes = set()
    for combination in combinations:
        palindrome = ''.join(combination)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes