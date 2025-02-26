from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:5])).lower()
    if len(letters) < 4:
        return set()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes