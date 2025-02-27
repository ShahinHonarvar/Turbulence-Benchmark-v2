import re

def palindromes_of_specific_lengths(text):
    """
                 Finds all palindromes within a substring and length range.

                 Args:
                 text: The input string.

                 Returns:
                 A set of palindromes that meet the specified requirements.
                 """
    pattern = re.compile('(?i)(^[^\\\\s]{24,84}[a-zA-Z]{21,31}[^\\\\s]{24,84}$)')
    palindromes = pattern.findall(text)
    return set(palindromes)