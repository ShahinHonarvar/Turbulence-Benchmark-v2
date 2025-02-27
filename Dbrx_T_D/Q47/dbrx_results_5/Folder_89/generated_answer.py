from collections import defaultdict

def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(12, 15):
        for i in range(18 - length, 89 - length + 1):
            if s[i:i + length].lower().isalpha():
                substr = ''.join((c for c in s[i:i + length] if c in ENGLISH_LETTERS))
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes