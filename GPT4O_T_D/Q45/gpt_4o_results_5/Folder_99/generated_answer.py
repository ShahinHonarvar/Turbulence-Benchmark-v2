from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    english_letters = [c.lower() for c in s[4:9] if c.isalpha()]
    if len(english_letters) < 3:
        return set()
    unique_palindromes = set()
    for length in range(3, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                unique_palindromes.add(perm_str)
    return unique_palindromes