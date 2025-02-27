from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    relevant_chars = [c for c in s[2:5] if c.isalpha()]
    if len(relevant_chars) < 3:
        return set()
    relevant_chars = [c.lower() for c in relevant_chars]
    all_permutations = set((''.join(p) for i in range(3, len(relevant_chars) + 1) for p in permutations(relevant_chars, i)))
    palindromes = {p for p in all_permutations if is_palindrome(p)}
    return palindromes