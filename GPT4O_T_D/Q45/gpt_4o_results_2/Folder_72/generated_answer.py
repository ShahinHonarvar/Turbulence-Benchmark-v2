from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    s = s[1:8].lower()
    valid_characters = [c for c in s if c.isalpha()]
    char_count = Counter(valid_characters)
    possible_palindromes = set()

    def can_form_palindrome(char_count, length):
        odds = sum((1 for count in char_count.values() if count % 2 != 0))
        return odds <= 1 if length % 2 == 0 else odds <= 1 or odds == 3
    if len(valid_characters) < 6:
        return possible_palindromes
    for perm in permutations(valid_characters, 6):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and can_form_palindrome(Counter(candidate), 6):
            possible_palindromes.add(candidate)
    return possible_palindromes