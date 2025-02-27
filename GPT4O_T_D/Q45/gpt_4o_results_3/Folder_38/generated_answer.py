from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    substring = s[3:9].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        potential_palindrome = ''.join(perm)
        if len(potential_palindrome) >= 5 and potential_palindrome == potential_palindrome[::-1]:
            palindromes.add(potential_palindrome)
    return palindromes