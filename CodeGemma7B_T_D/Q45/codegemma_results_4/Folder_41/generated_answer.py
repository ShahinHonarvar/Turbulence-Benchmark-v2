from itertools import permutations
  from string import ascii_letters

def palindromes_between_indices(text):
    text = text.lower()
    letters = [ch for ch in text if ch in ascii_letters]
    window = text[2:4]
    if not letters or window == text[0:4] or window == text[-4:]:
        return set()
    palindromes = set()
    for c in permutations(window):
        palindrome = ''.join(c)
        if palindrome in text:
            palindromes.add(palindrome)
    return palindromes