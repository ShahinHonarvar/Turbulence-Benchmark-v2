from itertools import permutations 
    import re

def palindromes_between_indices(string):
    substrings = set()
    for i in range(1, 9):
        subsets = list(permutations(string[i:9], i))
        for subset in subsets:
            substrings.add(''.join(subset))
    palindromes = set()
    for substring in substrings:
        substring = substring.lower()
        if substring == substring[::-1] and len(substring) >= 6:
            palindromes.add(substring)
    return palindromes