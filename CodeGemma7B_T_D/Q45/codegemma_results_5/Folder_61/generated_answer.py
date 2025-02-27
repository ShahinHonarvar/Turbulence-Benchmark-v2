from collections import defaultdict
from itertools import permutations

def palindromes_between_indices(text):
    letters = defaultdict(list)
    for index, char in enumerate(text):
        if char.isalpha():
            letters[char.lower()].append(index)

    def check_palindrome(lower_text):
        mid = len(lower_text) // 2
        return lower_text[:mid] == lower_text[mid + 1:]
    palindromes = set()
    seen = set()
    for char, indices in letters.items():
        if len(indices) < 7:
            continue
        for perm in permutations(indices):
            subseq = ''.join((text[i] for i in perm))
            if subseq not in seen and check_palindrome(subseq):
                palindromes.add(subseq)
                seen.add(subseq)
    return palindromes