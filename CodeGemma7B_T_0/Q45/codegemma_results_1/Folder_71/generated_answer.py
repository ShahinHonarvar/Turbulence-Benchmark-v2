import re
    from itertools import permutations

def palindromes_between_indices(text):
    """
    This function takes a string as input and returns a set of all palindromes of the length of at least 4 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 1 to index 3, both inclusive.
    """
    if not re.search('[a-zA-Z]', text[1:4]):
        return set()
    letters = re.findall('[a-zA-Z]', text[1:4])
    permutations_of_letters = set([''.join(p) for p in permutations(letters)])
    palindromes = set()
    for palindrome in permutations_of_letters:
        if len(palindrome) >= 4:
            palindromes.add(palindrome)
    return palindromes