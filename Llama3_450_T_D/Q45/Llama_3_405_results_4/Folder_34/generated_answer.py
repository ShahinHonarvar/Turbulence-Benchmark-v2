import itertools

def palindromes_between_indices(s):
    english_letters = [c.lower() for c in s[5:8] if c.isalpha()]
    palindromes = set()
    for r in range(4, len(english_letters) + 1):
        for permutation in itertools.permutations(english_letters, r):
            palindrome = ''.join(permutation)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes