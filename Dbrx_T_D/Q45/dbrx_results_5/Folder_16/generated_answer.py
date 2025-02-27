import re

def palindromes_between_indices(s: str) -> set:
    english_letters = set(re.findall('[a-zA-Z]', s[6:10]))
    palindromes = set()
    for length in range(5, len(english_letters) + 1):
        permutations = [''.join(p) for p in itertools.permutations(english_letters, length)]
        palindromes.update([p for p in permutations if p == p[::-1]])
    return palindromes