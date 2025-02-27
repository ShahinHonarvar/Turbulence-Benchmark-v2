from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:7] if c.isalpha()]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 6:
            palindromes.add(palindrome.lower())
    return palindromes