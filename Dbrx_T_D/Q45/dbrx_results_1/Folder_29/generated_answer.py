import itertools

def palindromes_between_indices(s):
    english_letters = {c.lower() for c in s if c.lower().isalpha()}
    if len(english_letters) < 2:
        return set()

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for length in range(6, len(english_letters) + 1):
        for combo in itertools.combinations(english_letters, length):
            combo = ''.join(combo)
            if is_palindrome(combo):
                palindromes.add(combo)
    return palindromes