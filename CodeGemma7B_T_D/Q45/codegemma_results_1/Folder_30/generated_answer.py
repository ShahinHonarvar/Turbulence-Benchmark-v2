from itertools import permutations

def palindromes_between_indices(s):
    palindromes = set()
    for p in permutations(s[0:5].lower()):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes