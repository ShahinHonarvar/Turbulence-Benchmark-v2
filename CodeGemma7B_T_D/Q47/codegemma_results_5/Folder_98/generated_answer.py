import re

def palindromes_of_specific_lengths(string):
    """
    This function returns the set of all palindromes in the substring from index 0 to index 20, both inclusive, with lengths between 5 to 80 (both inclusive).

    Args:
        string: The input string may consist of any character.

    Returns:
        The set of all palindromes that meet the specified requirements or an empty set if no such palindrome exists.
    """
    regex = re.compile('(?i)([a-z]{5,80})\\\\b')
    palindromes = regex.findall(string[0:21])
    return {palindrome for palindrome in palindromes if palindrome.lower() in string[0:21].lower()}