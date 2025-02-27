from itertools import product

def palindromes_between_indices(string):
    letters = sorted({c.lower() for c in string[2:7] if c.isalpha()})
    if len(letters) < 5:
        return set()
    palindromes = set()
    for letter in product(*letters):
        if letter[0] > letter[-1]:
            continue
        palindrome = ''.join(letter)
        if palindrome in palindromes:
            continue
        palindromes.add(palindrome)
    return palindromes