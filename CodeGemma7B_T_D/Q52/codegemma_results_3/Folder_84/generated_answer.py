import re

def palindrome_of_length_n(s):
    """
            Finds all palindromes of length n in a given string.

            Args:
            s: The string to search for palindromes in.

            Returns:
            A set of all palindromes of length n in the given string, or an empty set if no palindromes are found.
            """
    s = s.lower()
    pattern = re.compile('(?<=(\\\\w{n}))(\\\\w{n})$')
    matches = pattern.findall(s)
    palindromes = set()
    for match in matches:
        palindromes.add(match)
    return palindromes