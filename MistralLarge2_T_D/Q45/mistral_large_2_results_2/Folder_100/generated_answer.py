from itertools import permutations

def palindromes_between_indices(s):
    relevant_chars = [c for c in s[:6] if c.isalpha()]
    relevant_chars_lower = [c.lower() for c in relevant_chars]

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for length in range(6, len(relevant_chars_lower) + 1):
        for perm in permutations(relevant_chars_lower, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes