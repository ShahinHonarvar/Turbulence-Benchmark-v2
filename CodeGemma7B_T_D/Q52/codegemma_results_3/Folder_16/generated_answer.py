from itertools import combinations_with_replacement
from string import ascii_uppercase, ascii_lowercase

def palindrome_of_length_n(s: str) -> set:
    """
    Write a function called 'palindrome_of_length_n' that takes one argument, a string, and returns the set of all palindromes of the length equal to 255, where each palindrome is a substring of the given string. Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    lowercase_list = list(ascii_lowercase) + list(ascii_uppercase)
    uppercase_list = list(ascii_uppercase)
    combinations = set()
    for i in range(255):
        for comb in combinations_with_replacement(lowercase_list, i):
            combinations.add(''.join(comb))
        for comb in combinations_with_replacement(uppercase_list, i):
            combinations.add(''.join(comb))
    return {i for i in combinations if i in s.lower()}