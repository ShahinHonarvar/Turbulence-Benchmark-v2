from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[1:5])).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(4, len(substring) + 1):
        for perm in permutations(substring, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes