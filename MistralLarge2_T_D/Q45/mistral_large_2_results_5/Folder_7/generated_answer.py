import itertools

def palindromes_between_indices(s):
    s = s[1:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for combo in itertools.combinations(letters, length):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes