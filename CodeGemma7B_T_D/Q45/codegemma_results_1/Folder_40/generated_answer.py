from itertools import permutations

def palindromes_between_indices(s):
    letters = [letter for letter in s[4:10].lower() if letter in 'abcdefghijklmnopqrstuvwxyz']
    palindromes = set()
    for letters_ in permutations(letters):
        palindrome = ''.join(letters_)
        if len(palindrome) >= 7:
            palindromes.add(palindrome)
    return palindromes or set()