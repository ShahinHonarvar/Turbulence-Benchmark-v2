import itertools

def palindromes_between_indices(s):
    s = s[2:7].lower()
    s = ''.join(filter(str.isalpha, s))
    if len(s) < 3:
        return set()
    palindromes = set()
    for r in range(3, len(s) + 1):
        for t in itertools.permutations(s, r):
            palindrome = ''.join(t)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes