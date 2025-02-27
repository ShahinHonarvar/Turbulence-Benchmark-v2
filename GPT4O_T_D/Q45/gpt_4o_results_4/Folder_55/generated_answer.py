from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[:3].lower()
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for combo in permutations(substring, length):
            candidate = ''.join(combo)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes