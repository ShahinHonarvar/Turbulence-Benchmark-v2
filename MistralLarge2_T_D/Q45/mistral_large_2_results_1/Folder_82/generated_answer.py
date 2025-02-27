import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:7] if c.isalpha()]
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in itertools.permutations(letters, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes