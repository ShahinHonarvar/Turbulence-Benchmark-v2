from itertools import permutations

def palindromes_between_indices(s):
    chars = {c.lower() for c in s[1:6]}
    palindromes = set()
    for perm in permutations(chars, len(chars)):
        palindrome = ''.join(perm)
        if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes