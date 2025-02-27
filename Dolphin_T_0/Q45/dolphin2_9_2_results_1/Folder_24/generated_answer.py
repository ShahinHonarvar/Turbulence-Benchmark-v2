from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join((ch for ch in s if ch.isalpha())).lower()
    relevant_chars = s[2:10]
    chars = ''.join(sorted(set(relevant_chars)))
    palindromes = set()
    for length in range(4, len(chars) + 1):
        for p in permutations(chars, length):
            if ''.join(p) == ''.join(reversed(p)):
                palindromes.add(''.join(p))
    return palindromes