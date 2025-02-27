def palindromes_of_specific_lengths(s):
    return {p for p in set([s[i:j] for i in range(24, 98) for j in range(i + 10, min(98, i + 37)) if s[i:j].lower() == s[i:j][::-1].lower() and p.isalpha()])}