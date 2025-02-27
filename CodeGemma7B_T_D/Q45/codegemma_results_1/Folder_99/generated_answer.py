def palindromes_between_indices(string):
    """Given a string, return 
       the set of palindromes of 
       length of at least 3 from the
       characters at indices 4 to 8 
       inclusive, in case-insensitive
       manner.
    """
    return {word for word in permutations(set(string[4:8].lower())) if word == word[::-1] and len(word) >= 3}