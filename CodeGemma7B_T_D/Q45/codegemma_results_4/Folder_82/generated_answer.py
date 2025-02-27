from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(string):
    english_letters = set(ascii_lowercase)
    palindromes = set()
    for perm in permutations(string):
        palindrome = ''.join(perm)
        if palindrome.startswith('a') and palindrome.endswith('a') and (palindrome[1] == palindrome[5]) and (palindrome[2] == palindrome[4]) and all((letter in english_letters for letter in palindrome[1:6])) and (len(palindrome) >= 7):
            palindromes.add(palindrome)
    return palindromes