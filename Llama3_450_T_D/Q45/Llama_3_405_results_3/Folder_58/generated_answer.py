import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:7])).lower()
    letters = [s.count(c) for c in set(s)]
    palindromes = set()
    for p in itertools.product(*[c * l for c, l in zip(set(s), letters)]):
        palindrome = ''.join(p)
        if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes