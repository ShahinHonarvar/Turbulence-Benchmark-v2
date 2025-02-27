def palindromes_between_indices(s):
    english_letters = set((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(1, min(10, len(s) - 5)):
        for j in range(i, min(10, len(s) - i)):
            substring = s[i:j + 1]
            if len(substring) >= 7 and set(substring.lower()) <= english_letters:
                palindromes.add(''.join(sorted(substring.lower())))
    return palindromes