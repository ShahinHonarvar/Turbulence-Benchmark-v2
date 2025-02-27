from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    relevant_chars = [c.lower() for c in s[1:7] if c.isalpha()]
    palindromes = set()
    for length in range(3, len(relevant_chars) + 1):
        for perm in permutations(relevant_chars, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes