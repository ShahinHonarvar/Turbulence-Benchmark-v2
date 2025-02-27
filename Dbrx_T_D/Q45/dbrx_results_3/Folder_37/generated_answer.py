from itertools import permutations

def palindromes_between_indices(s):
    chars = set(s[1:5].lower())
    palindromes = set()
    for perm in permutations(chars, 5):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes