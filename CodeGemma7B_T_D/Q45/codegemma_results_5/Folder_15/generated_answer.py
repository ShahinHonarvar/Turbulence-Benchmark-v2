from itertools import product

def palindromes_between_indices(string):
    """
    Returns the set of all palindromes of the length of at least 3 such that each palindrome is created from 
    any possible arrangement of the English letters in the given string that occur between index 1 to index 2, both inclusive.
    """
    result = set()
    if len(string) < 3:
        return result
    start = 1
    end = 2
    combinations = product(*[list(string[i].lower()) for i in range(start, end + 1)])
    for combination in combinations:
        palindrome = ''.join(combination)
        result.add(palindrome)
    return result