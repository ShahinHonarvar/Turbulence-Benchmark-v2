from itertools import permutations

def palindromes_between_indices(string):
    palindromes = set()
    for indices in permutations(range(2, 9)):
        palindrome = ''.join((string[i].lower() for i in indices if string[i].isalpha()))
        if len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes