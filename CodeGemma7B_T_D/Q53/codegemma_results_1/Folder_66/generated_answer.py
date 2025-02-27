import re

def palindrome_of_length_at_least_n(text):
    """
    The function receives a list of strings, and it returns a set of all palindromes of length greater or equal to 76.
    In the function, it should use regular expressions to find all the palindromes of the mentioned length.
    """
    text = text.lower()
    palindromes = re.findall('(?i)(\\\\b[\\\\w]{76,})\\\\b', text)
    palindromes = set(palindromes)
    return palindromes