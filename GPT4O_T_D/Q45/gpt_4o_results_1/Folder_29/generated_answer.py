from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substr = s[2:10].lower()
    letter_substr = ''.join(filter(str.isalpha, substr))
    palindromes = set()
    for length in range(6, len(letter_substr) + 1):
        permuted_strs = set(permutations(letter_substr, length))
        for p in permuted_strs:
            permuted = ''.join(p)
            if is_palindrome(permuted):
                palindromes.add(permuted)
    return palindromes