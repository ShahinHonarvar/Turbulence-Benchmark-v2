def palindromes_between_indices(s):
    """Return the set of all palindromes created from any arrangement of 
    the English letters in the given string that occur between index 5 to 
    index 9, both inclusive, with length of at least 6."""

    def is_palindrome(w):
        return w == w[::-1]
    english_letters = [c for c in s[5:10] if c.isalpha()]
    arrangements = set(itertools.permutations(english_letters))
    palindromes = {''.join(a).lower() for a in arrangements if is_palindrome(a) and len(a) >= 6}
    return palindromes