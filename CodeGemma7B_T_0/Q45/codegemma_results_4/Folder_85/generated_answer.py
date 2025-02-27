import itertools
    from string import ascii_lowercase

def palindromes_between_indices(text):
    text = text.lower()
    letters = [char for char in text if char in ascii_lowercase and text.index(char) in range(2, 9)]
    if not letters:
        return set()
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes