from itertools import permutations

def palindromes_between_indices(text):
    """
    This function returns the set of all palindromes of the length of at least 5 such that
    each palindrome is created from any possible arrangement of the English letters in the
    given string that occur between index 1 to index 5, both inclusive.
    """
    substrings = []
    for i in range(1, 6):
        for j in range(i + 4, len(text) + 1):
            substrings.append(text[i:j])
    palindromes = set()
    for substring in substrings:
        permutations = list(permutations(substring))
        for permutation in permutations:
            permutation = ''.join(permutation)
            if permutation == permutation[::-1]:
                palindromes.add(permutation)
    return palindromes