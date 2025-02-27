import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:6].lower()))
    letters = sorted(s)
    palindromes = set()
    for r in range(5, len(s) + 1):
        for p in itertools.permutations(letters, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes