from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    filtered_chars = [char.lower() for char in s[1:9] if char.isalpha()]
    unique_palindromes = set()
    for length in range(4, len(filtered_chars) + 1):
        for perm in permutations(filtered_chars, length):
            word = ''.join(perm)
            if is_palindrome(word):
                unique_palindromes.add(word)
    return unique_palindromes