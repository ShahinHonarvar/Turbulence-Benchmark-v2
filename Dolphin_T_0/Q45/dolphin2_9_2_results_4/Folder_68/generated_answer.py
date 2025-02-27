import itertools
import string

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:9] if c in string.ascii_letters]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for subset in itertools.combinations(letters, length):
            for perm in itertools.permutations(subset):
                palindrome = ''.join(perm)
                if palindrome.lower() == palindrome.lower()[::-1]:
                    palindromes.add(palindrome)
    return palindromes