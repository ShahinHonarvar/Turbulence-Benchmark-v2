from collections import Counter
    from itertools import combinations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[0:6]
    letters = [char for char in substring if char.isalpha()]
    counter = Counter(letters.lower())
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for comb in combinations(letters, length):
            comb_str = ''.join(comb).lower()
            if is_palindrome(comb_str):
                palindromes.add(comb_str)
    return palindromes