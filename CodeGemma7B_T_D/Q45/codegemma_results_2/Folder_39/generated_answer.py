from itertools import permutations

def palindromes_between_indices(s):
    """
            This function forms the set of all palindromes of the length of at least 3 given from the string between index 2 to index 5, both inclusive, in a case-insensitive manner.
            """
    palindromes = set()
    s = s.lower()
    for letter in 'qwertyuiop':
        if letter not in s:
            return set()
    permutations_list = list(permutations(s[2:6]))
    for permutation in permutations_list:
        palindrome = ''.join(permutation)
        palindromes.add(palindrome)
    return palindromes