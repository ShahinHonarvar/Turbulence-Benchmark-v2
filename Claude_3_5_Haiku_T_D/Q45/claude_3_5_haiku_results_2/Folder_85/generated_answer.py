from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:9] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def can_form_palindrome(word):
        return len(word) >= 7 and is_palindrome(word)
    result = set()
    for length in range(7, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            word = ''.join(perm)
            for rearrangement in set(permutations(word)):
                candidate = ''.join(rearrangement)
                if can_form_palindrome(candidate):
                    result.add(candidate)
    return result