from collections import Counter
    from itertools import permutations

def palindromes_between_indices(text):

    def is_palindrome(word):
        return word[::-1].lower() == word.lower()
    substring = text[2:7]
    letters = [ch for ch in substring if ch.isalpha()]
    counter = Counter(letters)
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word.lower())
    return palindromes