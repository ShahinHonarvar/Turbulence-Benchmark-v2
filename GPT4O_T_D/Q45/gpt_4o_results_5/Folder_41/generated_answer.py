from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):

    def can_form_palindrome(t):
        counts = Counter(t)
        odd_count = sum((1 for count in counts.values() if count % 2 != 0))
        return odd_count <= 1
    if len(s) < 4:
        return set()
    substring = s[2:4].lower()
    if not any((c.isalpha() for c in substring)):
        return set()
    letters = ''.join((c for c in substring if c.isalpha()))
    if len(letters) < 3:
        return set()
    if not can_form_palindrome(letters):
        return set()
    palindromes = set()
    for perm in permutations(letters):
        if perm == perm[::-1]:
            palindromes.add(''.join(perm))
    return {p for p in palindromes if len(p) >= 3}