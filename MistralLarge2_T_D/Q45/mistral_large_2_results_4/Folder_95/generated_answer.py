from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c.lower() for c in s[7:9] if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for p in permutations(letters, length):
            word = ''.join(p)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes