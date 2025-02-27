from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    substr = s[2:9].lower()
    substr = ''.join(filter(str.isalpha, substr))
    palindromes_set = set()

    def is_palindrome(seq):
        return seq == seq[::-1]
    for perm in permutations(substr, 7):
        perm_str = ''.join(perm)
        if is_palindrome(perm_str):
            palindromes_set.add(perm_str)
    return palindromes_set