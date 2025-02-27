import re
    import itertools

def palindromes_between_indices(text):
    """
    This function takes a string as an argument and returns the set of all palindromes of the length of at least 5 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 1 to index 4, both inclusive. If no such palindromes of the specified length can be created from the English letters of the given string that occur in the specified range, the function should return an empty set. The function should form each palindrome in a case-insensitive manner.
    """
    letters = re.findall('[a-zA-Z]', text[1:5])
    if not letters:
        return set()
    arrangements = itertools.permutations(letters)
    palindromes = set()
    for arrangement in arrangements:
        palindrome = ''.join(arrangement)
        if len(palindrome) >= 5:
            palindromes.add(palindrome.lower())
    return palindromes