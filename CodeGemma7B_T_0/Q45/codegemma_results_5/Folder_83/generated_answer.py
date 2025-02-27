from itertools import permutations

def palindromes_between_indices(text):
    text = text.lower()
    letters = [letter for letter in text[2:10] if letter.isalpha()]
    if not letters:
        return set()
    palindromes = set()
    for letters in permutations(letters):
        palindrome = ''.join(letters)
        if palindrome in palindromes:
            continue
        if len(palindrome) >= 7:
            palindromes.add(palindrome)
    return palindromes