import itertools

def palindromes_between_indices(string):
    substring = string[6:10]
    substring = substring.lower()
    letters = [letter for letter in substring if letter.isalpha()]
    if not letters:
        return set()
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome)
    return palindromes