from itertools import permutations, combinations

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[3:8] if c.isalpha()])
    longest_palindromes = set()
    for length in range(5, len(letters) + 1):
        for palindrome in combinations(letters, length):
            if ''.join(palindrome) == ''.join(palindrome[::-1]):
                longest_palindromes.add(''.join(palindrome))
    return longest_palindromes