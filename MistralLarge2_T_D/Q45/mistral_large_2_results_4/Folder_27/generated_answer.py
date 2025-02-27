from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    relevant_chars = [char for char in s[2:9] if char.isalpha()]
    relevant_chars = [char.lower() for char in relevant_chars]
    palindromes = set()
    for length in range(6, len(relevant_chars) + 1):
        for perm in permutations(relevant_chars, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes