from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s = s[:7]
    filtered_chars = ''.join([c.lower() for c in s if c.isalpha()])
    palindromes = set()
    for perm in permutations(filtered_chars, len(filtered_chars)):
        perm_str = ''.join(perm)
        if len(perm_str) >= 7 and is_palindrome(perm_str):
            palindromes.add(perm_str)
    return palindromes