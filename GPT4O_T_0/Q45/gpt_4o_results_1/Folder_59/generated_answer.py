from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[8:10].lower()

    def is_palindrome(word):
        return word == word[::-1]
    letter_counts = Counter(filter(str.isalpha, substring))
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for perm in permutations(substring, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindromes.add(perm_str)
    return palindromes