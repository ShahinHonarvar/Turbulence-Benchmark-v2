from collections import Counter
  from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[1:5] if c.isalpha())).lower()
    letters_count = Counter(letters)
    palindromes = set()
    for perm in permutations(letters):
        candidate = ''.join(perm)
        if len(candidate) >= 5 and candidate == candidate[::-1] and (not any((letters_count[c] < candidate.count(c) for c in set(candidate)))):
            palindromes.add(candidate)
    return palindromes