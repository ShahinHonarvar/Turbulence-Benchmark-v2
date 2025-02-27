import itertools

def palindromes_between_indices(string):
    letters = [char for char in string[3:8] if char.isalpha()]
    permutations = itertools.permutations(letters)
    palindromes = []
    for permutation in permutations:
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1] and len(palindrome) >= 5:
            palindromes.append(palindrome)
    return set(palindromes)