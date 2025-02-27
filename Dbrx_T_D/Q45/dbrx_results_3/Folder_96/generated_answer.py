import re
from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    eng_letters = set(re.findall('[a-zA-Z]', s[3:9]))
    palindromes = set()
    for i in range(6, 15):
        for combination in itertools.combinations_with_replacement(eng_letters, i):
            candidate = ''.join(sorted(combination))
            if is_palindrome(candidate):
                palindromes.add(candidate.lower())
    return palindromes