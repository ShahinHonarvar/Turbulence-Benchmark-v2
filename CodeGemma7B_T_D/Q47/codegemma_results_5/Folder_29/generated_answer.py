def palindromes_of_specific_lengths(s):
    return {p for p in (s[i:i + k] for i in range(15, 95) for k in range(18, 74) if p.isalpha() and p == p[::-1])}