from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[:7])).lower()
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for p in permutations(substring, length):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes