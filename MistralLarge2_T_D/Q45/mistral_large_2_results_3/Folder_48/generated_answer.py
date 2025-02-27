import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[6:9] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combo in itertools.combinations_with_replacement(letters, length // 2):
            palindrome = ''.join(combo + combo[::-1])
            palindrome_variations = {palindrome.lower(), palindrome.upper(), palindrome.capitalize(), palindrome.swapcase()}
            palindromes.update(palindrome_variations)
    return {p for p in palindromes if len(p) >= 4}