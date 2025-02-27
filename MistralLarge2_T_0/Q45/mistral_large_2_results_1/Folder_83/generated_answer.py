import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:10] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for combo in itertools.combinations_with_replacement(letters, length):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes