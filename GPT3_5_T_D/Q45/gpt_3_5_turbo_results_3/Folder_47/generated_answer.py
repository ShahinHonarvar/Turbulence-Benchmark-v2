from itertools import permutations

def palindromes_between_indices(string):
    palindromes = set()
    letters = [char.lower() for char in string[3:8] if char.isalpha()]
    if len(letters) < 5:
        return palindromes
    for perm in permutations(letters):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome.lower())
    return palindromes