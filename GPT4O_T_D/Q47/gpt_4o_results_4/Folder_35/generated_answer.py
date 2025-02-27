def palindromes_of_specific_lengths(s):
    substr = s[34:91].lower()
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 14, min(i + 40, len(substr) + 1)):
            segment = substr[i:j]
            alpha_only = ''.join((c for c in segment if c.isalpha()))
            if len(alpha_only) >= 14 and alpha_only == alpha_only[::-1]:
                palindromes.add(alpha_only)
    return palindromes