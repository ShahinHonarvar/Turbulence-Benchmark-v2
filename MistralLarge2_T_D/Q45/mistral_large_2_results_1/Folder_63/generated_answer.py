import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[:4] if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            mid = length // 2
            if combination[:mid] == combination[-mid:][::-1]:
                palindrome = ''.join(combination).lower()
                palindromes.add(palindrome)
    return palindromes