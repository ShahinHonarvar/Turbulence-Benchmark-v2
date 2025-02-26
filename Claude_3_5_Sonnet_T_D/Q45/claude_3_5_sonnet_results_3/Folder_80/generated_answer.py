from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    letters = ''.join((c for c in s[3:9] if c.isalpha()))
    letters = letters.lower()
    palindromes = set()
    for i in range(7, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes