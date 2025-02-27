import itertools
    import re

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string[1:9])
    permutations = set(itertools.permutations(letters, len(letters)))
    palindromes = set()
    for perm in permutations:
        palindrome = ''.join(perm) + ''.join(perm)[::-1]
        if len(palindrome) >= 7:
            palindromes.add(palindrome.lower())
    return palindromes