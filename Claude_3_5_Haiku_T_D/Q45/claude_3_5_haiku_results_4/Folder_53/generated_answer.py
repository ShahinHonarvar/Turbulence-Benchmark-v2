from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:9] if char.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]
    palindrome_set = set()
    for length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for arrangement in set(permutations(perm)):
                word = ''.join(arrangement)
                if is_palindrome(word) and len(word) >= 6:
                    palindrome_set.add(word)
    return palindrome_set