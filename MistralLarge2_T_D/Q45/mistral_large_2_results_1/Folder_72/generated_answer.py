from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(p):
        return p == p[::-1]
    substring = ''.join(filter(str.isalpha, s[1:8])).lower()
    unique_chars = set(substring)
    palindromes = set()
    for length in range(6, len(substring) + 1):
        for combination in permutations(unique_chars, length):
            palindrome = ''.join(combination)
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes