from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[5:8] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        palindrome = ''.join(perm)
        if len(palindrome) > 2 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome.lower())
    return palindromes