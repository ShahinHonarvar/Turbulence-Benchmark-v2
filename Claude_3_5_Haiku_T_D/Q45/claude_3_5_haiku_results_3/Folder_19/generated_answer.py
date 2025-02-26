from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [char.lower() for char in s[1:8] if char.isalpha()]
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for rearrangement in set(permutations(perm)):
                word = ''.join(rearrangement)
                if is_palindrome(word):
                    palindromes.add(word)
    return palindromes