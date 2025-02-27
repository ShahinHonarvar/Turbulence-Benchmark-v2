from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(text):
    text = text.lower()
    letters = [letter for letter in text[2:10] if letter in ascii_lowercase]
    if not letters:
        return set()
    palindromes = set()
    for letters in permutations(letters):
        palindrome = ''.join(letters)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes