import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[1:6] if c.isalpha()]
    if len(letters) < 6:
        return set()
    letters = [c.lower() for c in letters]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes