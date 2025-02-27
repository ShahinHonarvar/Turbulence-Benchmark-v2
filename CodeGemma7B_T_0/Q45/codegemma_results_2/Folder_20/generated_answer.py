from itertools import permutations

def palindromes_between_indices(text):
    text = text.lower()
    letters = [char for char in text[2:9] if char.isalpha()]
    if not letters:
        return set()
    palindromes = set()
    for letters in permutations(letters):
        palindrome = ''.join(letters)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes