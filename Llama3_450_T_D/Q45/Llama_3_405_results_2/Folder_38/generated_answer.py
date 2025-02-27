import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[3:9])).lower()
    if len(s) < 5:
        return set()
    letters = sorted(s)
    palindromes = set()
    for r in range(5, len(s) + 1):
        for combo in itertools.combinations_with_replacement(letters, r):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes