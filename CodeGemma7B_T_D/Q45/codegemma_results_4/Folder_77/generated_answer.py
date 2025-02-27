def palindromes_between_indices(s):
    """
    Return the set of all palindromes of the length of at least 4
    such that each palindrome is created from any possible arrangement
    of the English letters in the given string that occur between
    index 4 to index 6, both inclusive.
    """

    def is_palindrome(s):
        return s == s[::-1]

    def get_letters_in_range(s, start, end):
        letters = []
        for i in range(start, end + 1):
            if s[i].isalpha():
                letters.append(s[i].lower())
        return letters
    letters = get_letters_in_range(s, 4, 6)
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if is_palindrome(palindrome):
            palindromes.add(palindrome)
    return palindromes