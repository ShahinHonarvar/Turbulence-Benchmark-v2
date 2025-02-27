from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:6]
    letters = [c.lower() for c in s if c.isalpha()]
    unique_palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(3, len(letters) + 1):
        for p in permutations(letters, length):
            word = ''.join(p)
            if is_palindrome(word):
                unique_palindromes.add(word)
    return unique_palindromes