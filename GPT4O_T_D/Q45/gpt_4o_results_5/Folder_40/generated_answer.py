from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    sub_string = ''.join((c.lower() for c in s[4:10] if c.isalpha()))
    if len(sub_string) < 7:
        return set()
    palindromes = set()
    for perm in set(permutations(sub_string, 7)):
        perm_string = ''.join(perm)
        if is_palindrome(perm_string):
            palindromes.add(perm_string)
    return palindromes