from collections import defaultdict
from itertools import product

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    char_to_indices = defaultdict(list)
    for i, char in enumerate(s):
        char_to_indices[char].append(i)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 45, len(s) + 1):
            for indices in product(*(char_to_indices[c] for c in s[i:j])):
                if all((idx[0] < idx[1] for idx in zip(indices, indices[1:]))):
                    palindromes.add(s[i:j])
    return palindromes