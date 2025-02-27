from itertools import permutations

def palindromes_between_indices(text):
    """
    Returns the set of all palindromes of the length of at least 4 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 2 to index 8, both inclusive.
    """
    letters = sorted([char.lower() for char in text[2:9]], key=str.casefold)
    arrangements = permutations(letters)
    palindromes = []
    for arrangement in arrangements:
        palindrome = ''.join(arrangement)
        if len(palindrome) >= 4:
            palindromes.append(palindrome)
    return set(palindromes)