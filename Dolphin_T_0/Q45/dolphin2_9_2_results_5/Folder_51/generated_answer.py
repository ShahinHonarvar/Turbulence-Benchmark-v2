from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:6]
    palindromes = set()
    for perm in permutations(substring, len(substring)):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome.lower())
    return palindromes