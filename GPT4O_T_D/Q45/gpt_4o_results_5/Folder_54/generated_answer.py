from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[4:10].lower()
    letters = [ch for ch in substring if ch.isalpha()]

    def can_form_palindrome(counts):
        odd_count = sum((1 for count in counts.values() if count % 2 != 0))
        return odd_count <= 1
    letter_counts = Counter(letters)
    if not letters or not can_form_palindrome(letter_counts):
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes