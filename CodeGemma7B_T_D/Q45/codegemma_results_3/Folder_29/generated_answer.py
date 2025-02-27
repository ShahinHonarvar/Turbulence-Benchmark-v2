from itertools import permutations

def palindromes_between_indices(s):
    """
    :type s: str
    :rtype: set[str]
    """
    letters = [c.lower() for c in s[2:10]]
    palindromes = set()
    for p in permutations(letters):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1] and len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes