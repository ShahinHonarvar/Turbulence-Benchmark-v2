def palindromes_between_indices(s):
    letters = ''.join((c for c in s[:6] if c.isalpha())).lower()
    palindromes = set()
    for i in range(3, len(letters) + 1):
        combinations = set((letters[j:j + i] for j in range(len(letters) - i + 1)))
        palindromes.update((word for word in combinations if word == word[::-1]))
    return palindromes