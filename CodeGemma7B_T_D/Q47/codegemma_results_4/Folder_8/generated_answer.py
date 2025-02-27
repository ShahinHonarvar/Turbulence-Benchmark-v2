def palindromes_of_specific_lengths(text):
    """
    The function finds palindromes of lengths between
    50 to 51 (inclusive) in the substring from
    index 17 to index 72, both inclusive, of the
    given text, ignoring cases and punctuation.

    The function returns a set of palindromes. If no palindrome
    of the required length occurs in the given range, the
    function returns an empty set.
    """

    def is_palindrome(word):
        """
        Checks if a word is a palindrome.

        The function returns True if the word is a palindrome,
        False otherwise.
        """
        word = ''.join((char.lower() for char in word if char.isalpha()))
        return word == word[::-1]
    substring = text[16:73]
    palindromes = set()
    for i in range(len(substring) - 50):
        for j in range(i + 50, len(substring) + 1):
            word = substring[i:j]
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes