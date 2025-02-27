import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:7] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combo in itertools.permutations(letters, length):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes