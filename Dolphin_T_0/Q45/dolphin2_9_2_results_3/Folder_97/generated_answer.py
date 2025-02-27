import itertools
    import string

def palindromes_between_indices(string):
    palindromes = set()
    for combination in itertools.combination(string.ascii_lowercase, 3):
        palindrome = ''.join(combination) + palindrome[::-1] in string.lower()
        if palindrome:
            palindromes.add(palindrome)
    return palindromes