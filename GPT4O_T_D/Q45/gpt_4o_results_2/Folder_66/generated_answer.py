from itertools import permutations

def palindromes_between_indices(string):

    def is_palindrome(s):
        return s == s[::-1]
    substring = ''.join(filter(str.isalpha, string[:6])).lower()
    palindromes = set()
    for length in range(5, len(substring) + 1):
        for perm in permutations(substring, length):
            permuted_str = ''.join(perm)
            if is_palindrome(permuted_str):
                palindromes.add(permuted_str)
    return palindromes