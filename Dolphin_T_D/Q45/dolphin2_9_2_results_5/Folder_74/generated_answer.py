from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join([c for c in s if c.isalpha()])
    s = s[1:7]
    palindrome_set = set()
    if len(s) < 3:
        return palindrome_set
    for p in permutations(s, len(s)):
        s = ''.join(p)
        for i in range(len(s)):
            palindrome = s[i:] + s[:i]
            if palindrome == palindrome[::-1] and len(palindrome) >= 6:
                palindrome_set.add(palindrome)
    return palindrome_set