def palindromes_between_indices(s):
    english_letters = set((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(1, len(s)):
        for j in range(i + 1, min(i + 4, len(s))):
            substring = s[i:j + 1]
            if english_letters.issuperset(set(substring.lower())):
                palindromes.add(''.join(sorted(substring.lower())))
    return palindromes