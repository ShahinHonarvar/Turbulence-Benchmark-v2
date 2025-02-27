import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:10] if c.isalpha()]
    if len(letters) == 0:
        return set()
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for combo in itertools.permutations(letters, length):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes