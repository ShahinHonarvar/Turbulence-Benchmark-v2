from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[3:9] if c.isalpha()]).lower()
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for p in permutations(letters, length):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes