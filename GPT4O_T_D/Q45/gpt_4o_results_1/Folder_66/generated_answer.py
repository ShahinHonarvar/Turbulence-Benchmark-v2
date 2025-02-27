from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    end_index = min(6, len(s))
    filtered_chars = [char.lower() for char in s[0:end_index] if char.isalpha()]
    if len(filtered_chars) < 5:
        return set()
    palindromes = set()
    for length in range(5, min(7, len(filtered_chars) + 1)):
        for perm in set(permutations(filtered_chars, length)):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes