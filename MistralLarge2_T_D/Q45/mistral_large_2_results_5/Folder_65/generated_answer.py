import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[0:7] if c.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for combination in itertools.combinations_with_replacement(letters, length):
            if combination == combination[::-1]:
                palindrome = ''.join(combination)
                palindromes.add(palindrome)
    return palindromes