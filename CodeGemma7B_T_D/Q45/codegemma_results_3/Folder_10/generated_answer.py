from itertools import permutations

def palindromes_between_indices(string):
    palindromes = set()
    for permutation in permutations(string[0:6]):
        palindrome = ''.join([char for char in permutation if char.isalpha()])
        if palindrome != '' and palindrome == palindrome[::-1]:
            palindromes.add(palindrome.lower())
    return palindromes