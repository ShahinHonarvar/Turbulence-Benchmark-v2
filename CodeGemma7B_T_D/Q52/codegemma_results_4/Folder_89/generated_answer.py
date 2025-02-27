from typing import Set

def palindrome_of_length_n(text: str) -> Set[str]:
    """
    The function takes in a string as input and returns a set of all the palindromes of the length equal to 4.

    :param text: The string to search for palindromes in.
    :type text: str

    :returns: A set of strings containing all the palindromes of the length 4 or an empty set.
    :rtype: Set[str]
    """
    text = text.lower()
    result = set()
    for i in range(len(text) - 3):
        for j in range(i + 1, len(text) - 2):
            for k in range(j + 1, len(text) - 1):
                for l in range(k + 1, len(text)):
                    if text[i] == text[l] and text[j] == text[k]:
                        result.add(text[i:l + 1])
    return result