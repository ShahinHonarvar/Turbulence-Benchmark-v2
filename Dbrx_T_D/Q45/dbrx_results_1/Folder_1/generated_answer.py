import re
from collections import Set

def palindromes_between_indices(s: str) -> Set[str]:
    english_letters = set(re.findall('[a-zA-Z]', s[4:8]))
    if len(english_letters) < 5:
        return set()
    permutations = [''.join(p) for i in range(5, len(english_letters) + 1) for p in itertools.permutations(english_letters, i)]
    palindromes = [p for p in permutations if p == p[::-1]]
    return set((palindrome.lower() for palindrome in palindromes))