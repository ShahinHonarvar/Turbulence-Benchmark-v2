import re
    from typing import Set

def palindrome_of_length_at_least_n(txt):
    """
    find all palindromes of the length greater than or equal to 141 in a string
    """

    def is_palindrome(word: str) -> bool:
        """
        check if a word is a palindrome
        """
        return word == word[::-1]
    word = re.findall('[a-zA-Z]+', txt)
    if not word:
        return set()
    res = set()
    for w in word:
        if len(w) >= 141 and is_palindrome(w.lower()):
            res.add(w.lower())
    return res