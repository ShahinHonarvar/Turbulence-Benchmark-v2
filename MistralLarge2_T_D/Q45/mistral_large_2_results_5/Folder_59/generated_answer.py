from itertools import permutations

def palindromes_between_indices(s):
    letters = [ch.lower() for ch in s[8:10] if ch.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes