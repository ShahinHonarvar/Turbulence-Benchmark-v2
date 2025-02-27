import itertools

def palindromes_between_indices(s):
    s = s[3:10].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(3, len(s) + 1):
        for c in itertools.combinations(s, r):
            for p in itertools.permutations(c):
                palindrome = ''.join(p)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes