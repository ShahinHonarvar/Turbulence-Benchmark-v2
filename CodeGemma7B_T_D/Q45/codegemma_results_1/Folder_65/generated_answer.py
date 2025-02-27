from itertools import permutations

def palindromes_between_indices(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    filtered_s = ''.join([char for char in s if char in alphabet]).lower()
    filtered_slice = filtered_s[0:7]
    palindromes = set()
    for permutation in permutations(filtered_slice):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 5:
            palindromes.add(palindrome)
    return palindromes