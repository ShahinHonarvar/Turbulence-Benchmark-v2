import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[4:10] if c.isalpha()]
    letters_lower = [c.lower() for c in letters]
    palindromes = set()
    for length in range(6, len(letters_lower) + 1):
        for comb in itertools.combinations(letters_lower, length):
            palindrome = ''.join(comb)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes