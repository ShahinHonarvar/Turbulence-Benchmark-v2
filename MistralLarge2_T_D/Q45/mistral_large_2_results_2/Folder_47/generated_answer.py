import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[3:8] if c.isalpha()]
    letters = [c.lower() for c in letters]
    if len(letters) < 5:
        return set()
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            if combination == combination[::-1]:
                palindrome = ''.join(combination)
                palindromes.add(palindrome)
    return palindromes