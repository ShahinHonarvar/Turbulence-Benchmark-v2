from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[1:8] if c.isalpha()]
    if len(letters) < 5:
        return set()
    counter = Counter(letters)
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            palindrome = ''.join(perm).lower()
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes