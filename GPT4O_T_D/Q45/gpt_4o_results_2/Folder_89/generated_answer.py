from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    relevant_part = ''.join(filter(str.isalpha, s[5:10])).lower()
    palindromes_set = set()
    if len(relevant_part) < 6:
        return set()
    for length in range(6, len(relevant_part) + 1):
        for perm in permutations(relevant_part, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindromes_set.add(perm_str)
    return palindromes_set