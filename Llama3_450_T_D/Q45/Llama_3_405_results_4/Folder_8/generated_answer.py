import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:6] if c.isalpha()]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for combination in itertools.permutations(letters, r):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes