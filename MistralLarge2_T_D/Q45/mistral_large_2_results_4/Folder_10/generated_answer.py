import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:6])).lower()
    perms = set(itertools.permutations(letters, len(letters)))
    palindromes = set()
    for p in perms:
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome)
    return palindromes