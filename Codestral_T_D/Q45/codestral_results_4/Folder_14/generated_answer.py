from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:6].lower()
    palindromes = set()
    for p in permutations(s):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome)
    return palindromes