from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [char.lower() for char in s[:5] if char.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for p in set(permutations(perm)):
                word = ''.join(p)
                if is_palindrome(word):
                    palindromes.add(word)
    return palindromes