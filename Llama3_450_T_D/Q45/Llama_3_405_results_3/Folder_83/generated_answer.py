import itertools

def palindromes_between_indices(s):
    s = s[2:10].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(7, len(s) + 1):
        for perm in itertools.permutations(s, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes