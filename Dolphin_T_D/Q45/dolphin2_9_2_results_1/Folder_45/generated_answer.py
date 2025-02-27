from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[4:10]))
    palindromes = set()
    for p in range(4, len(letters) + 1):
        for t in permutations(letters, p):
            for h in set(t):
                palindrome = ''.join(h * 2)
                if palindrome[::-1] == palindrome and palindrome not in palindromes:
                    palindromes.add(palindrome)
    return palindromes