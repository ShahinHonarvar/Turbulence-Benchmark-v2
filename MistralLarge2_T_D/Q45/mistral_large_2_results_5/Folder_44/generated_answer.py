from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(string):
        return string == string[::-1]
    substring = ''.join(filter(str.isalpha, s[2:8])).lower()
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for perm in permutations(substring, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes