from itertools import permutations

def palindromes_between_indices(text):
    """
  Creates a set of all palindromes of the length of at least 6 from the given string between index 1 to index 7, both inclusive.
  """
    letters = [char.lower() for char in text[1:8] if char.isalpha()]
    if len(letters) < 6:
        return set()
    permutations_of_letters = permutations(letters)
    palindromes = set()
    for permutation in permutations_of_letters:
        palindrome = ''.join(permutation)
        if len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes