from itertools import permutations

def palindromes_between_indices(text):
    text = text[2:9].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    valid_palindromes = set()
    for permutation in permutations(text):
        palindrome = ''.join(permutation)
        if palindrome in english_letters:
            valid_palindromes.add(palindrome)
    return valid_palindromes