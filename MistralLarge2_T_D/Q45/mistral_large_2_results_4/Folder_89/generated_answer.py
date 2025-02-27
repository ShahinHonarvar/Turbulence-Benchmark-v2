import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:10] if c.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for combo in itertools.combinations_with_replacement(letters, length):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes