from itertools import permutations

def palindromes_between_indices(s):
    valid_chars = s[4:10].lower()
    char_counts = {}
    for char in valid_chars:
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    half_palindrome = []
    odd_char = None
    for char, count in char_counts.items():
        half_palindrome.extend(char * (count // 2))
        if count % 2 == 1:
            if odd_char:
                return set()
            odd_char = char
    half_permutations = set(permutations(half_palindrome, len(half_palindrome)))
    palindromes = set()
    for half in half_permutations:
        full = ''.join(half) + (odd_char if odd_char else '') + ''.join(half[::-1])
        if len(full) >= 6:
            palindromes.add(full)
    return palindromes