from itertools import permutations

def palindromes_between_indices(text):
    letters = [char for char in text if char.isalpha() and 3 <= text.index(char) <= 9]
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome.lower())
    return palindromes