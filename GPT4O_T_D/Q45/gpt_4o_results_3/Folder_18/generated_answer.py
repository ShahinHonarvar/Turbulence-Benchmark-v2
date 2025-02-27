from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    sub_string = ''.join((c.lower() for c in s[1:7] if c.isalpha()))
    if len(sub_string) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(sub_string) + 1):
        for perm in set(permutations(sub_string, length)):
            joined_perm = ''.join(perm)
            if is_palindrome(joined_perm):
                palindromes.add(joined_perm)
    return palindromes