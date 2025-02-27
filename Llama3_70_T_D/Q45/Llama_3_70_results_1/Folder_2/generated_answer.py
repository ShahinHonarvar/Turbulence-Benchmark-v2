from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        palindrome = ''.join(p)
        for i in range(len(palindrome) // 2 + 1, len(palindrome) + 1):
            if len(palindrome) >= 6 and palindrome[:i] == palindrome[i:][::-1]:
                palindromes.add(palindrome)
    return palindromes