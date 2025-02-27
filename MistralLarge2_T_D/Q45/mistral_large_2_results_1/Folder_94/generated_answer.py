import re
    from itertools import permutations

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[3:5])
    letters = ''.join(letters).lower()
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes