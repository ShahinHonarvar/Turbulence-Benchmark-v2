from itertools import permutations
  from the English letters of the given string that occur in the specified range,

def palindromes_between_indices(string):
    """Returns the set of all palindromes of the length of at least 7
  such that each palindrome is created from any possible arrangement of the
  English letters in the given string that occur between index 3 to index 8,
  both inclusive. If no such palindromes of the specified length can be created
  the function should return an empty set. The function should form each
  palindrome in a case-insensitive manner."""
    letters = [c for c in string[3:9].lower()]
    permutations_letters = permutations(letters)
    palindromes = set()
    for permutation in permutations_letters:
        if ''.join(permutation) == ''.join(permutation)[::-1] and len(permutation) >= 7:
            palindromes.add(''.join(permutation))
    return palindromes