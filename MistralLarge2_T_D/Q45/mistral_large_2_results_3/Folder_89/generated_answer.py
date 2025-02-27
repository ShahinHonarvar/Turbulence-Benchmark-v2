from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    relevant_chars = [char for char in s[5:10] if char.isalpha()]
    if len(relevant_chars) < 6:
        return set()
    lower_chars = [char.lower() for char in relevant_chars]
    palindromes = set()
    for perm in permutations(lower_chars):
        word = ''.join(perm)
        if is_palindrome(word) and len(word) >= 6:
            palindromes.add(word)
    return palindromes