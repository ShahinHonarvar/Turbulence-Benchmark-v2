from itertools import permutations

def palindromes_between_indices(str):
    letters = [c for c in str[6:10].lower() if c.isalpha()]
    if not letters:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        palindrome = ''.join(perm)
        if palindrome not in palindromes and palindrome[::-1] not in palindromes:
            palindromes.add(palindrome)
    return palindromes