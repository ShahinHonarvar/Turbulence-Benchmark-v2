import itertools

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    english_letters = [c for c in substring if c.isalpha()]
    palindromes = set()
    for length in range(6, len(english_letters) + 1):
        for combo in itertools.combinations(english_letters, length):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes