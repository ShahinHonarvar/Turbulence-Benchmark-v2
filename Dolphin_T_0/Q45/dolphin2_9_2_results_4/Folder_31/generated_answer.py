import itertools
import string

def palindromes_between_indices(s):
    s_indices = s[1:9]
    s_indices_lower = ''.join((c.lower() for c in s_indices if c in string.ascii_letters))
    palindromes = set()
    for i in range(6, len(s_indices_lower) + 1):
        for subset in itertools.combinations(s_indices_lower, i):
            for perm in itertools.permutations(subset):
                palindrome = ''.join(perm)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes