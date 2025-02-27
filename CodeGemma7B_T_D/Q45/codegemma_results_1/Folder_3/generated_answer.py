from itertools import permutations

def palindromes_between_indices(word):
    if not isinstance(word, str):
        raise TypeError('Input must be a string')
    indices = [7, 8, 9]
    letters = [char.lower() for i, char in enumerate(word) if i in indices]
    if not letters:
        return set()
    palindromes = set()
    for p in permutations(letters, len(letters)):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes