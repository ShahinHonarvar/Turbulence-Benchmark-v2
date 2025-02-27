import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[6:10] if c.isalpha()]
    unique_letters = set((c.lower() for c in letters))
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combo in itertools.combinations_with_replacement(unique_letters, length // 2):
            palindrome = ''.join(combo + combo[-(length // 2 + length % 2):-1])
            palindromes.add(palindrome)
    return palindromes