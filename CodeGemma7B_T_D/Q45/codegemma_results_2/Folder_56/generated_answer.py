from itertools import permutations

def palindromes_between_indices(string):
    palindrome = permutations(string[5:10].lower())
    arr = {''.join(x) for x in palindrome}
    return arr