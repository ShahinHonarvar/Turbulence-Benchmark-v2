from itertools import permutations
    from string import ascii_letters

def palindromes_between_indices(s):
    substring = s[3:8]
    filtered_chars = [c for c in substring if c in ascii_letters]

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for length in range(4, len(filtered_chars) + 1):
        for perm in permutations(filtered_chars, length):
            word = ''.join(perm).lower()
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes