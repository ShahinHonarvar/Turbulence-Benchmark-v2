from itertools import permutations
    from collections import defaultdict

def palindromes_between_indices(text):

    def is_palindrome(text):
        text = text.lower()
        return text == text[::-1]
    letters = defaultdict(int)
    for char in text[1:7]:
        letters[char.lower()] += 1
    palindromes = set()
    for perm in permutations(letters.keys()):
        palindrome = ''.join(perm) * letters[perm[0]]
        if is_palindrome(palindrome):
            palindromes.add(palindrome)
    return palindromes