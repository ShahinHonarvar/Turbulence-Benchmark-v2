import itertools

def palindromes_between_indices(s):
    s = s[0:5].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(3, len(s) + 1):
        for p in itertools.permutations(s, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes