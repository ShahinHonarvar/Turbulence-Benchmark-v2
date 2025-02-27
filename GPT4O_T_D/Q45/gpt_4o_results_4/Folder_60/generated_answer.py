from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(st):
        return st == st[::-1]
    if len(s) < 7:
        return set()
    substring = s[3:7].lower()
    letters_count = Counter(filter(str.isalpha, substring))
    palindromes = set()
    for i in range(4, len(letters_count) + 1):
        for perm in permutations(letters_count.elements(), i):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindromes.add(perm_str)
    return palindromes