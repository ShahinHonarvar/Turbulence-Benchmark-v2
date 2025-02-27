import itertools

def palindromes_between_indices(s):
    english_chars = [c.lower() for c in s[4:9] if c.isalpha()]
    if len(english_chars) < 5:
        return set()
    palindromes = set()
    for r in range(5, len(english_chars) + 1):
        for perm in itertools.permutations(english_chars, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes