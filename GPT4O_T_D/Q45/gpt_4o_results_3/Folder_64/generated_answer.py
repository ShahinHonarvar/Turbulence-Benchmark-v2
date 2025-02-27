from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()

    def is_palindrome(word):
        return word == word[::-1]
    letters_only = ''.join(filter(str.isalpha, s))
    if len(letters_only) < 5:
        return set()
    char_count = Counter(letters_only)
    odd_count = sum((1 for count in char_count.values() if count % 2 != 0))
    if odd_count > 1:
        return set()
    perms = set(permutations(letters_only))
    valid_palindromes = {''.join(p) for p in perms if is_palindrome(''.join(p)) and len(p) >= 5}
    return valid_palindromes