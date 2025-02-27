import re
import itertools

def palindromes_between_indices(s):
    english_letters = re.findall('[a-zA-Z]', s[:8])
    letters = ''.join(english_letters).lower()
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                palindrome = ''.join(perm)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes