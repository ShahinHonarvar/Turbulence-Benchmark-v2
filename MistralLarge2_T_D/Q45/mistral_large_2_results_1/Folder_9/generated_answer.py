from itertools import permutations

def palindromes_between_indices(string):
    substr = ''.join((c for c in string[:7] if c.isalpha())).lower()
    palindromes = set()
    for length in range(7, len(substr) + 1):
        for perm in permutations(substr, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes