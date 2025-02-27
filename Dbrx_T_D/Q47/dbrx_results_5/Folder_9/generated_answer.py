def palindromes_of_specific_lengths(s):
    s = ''.join((c.lower() for c in s if c.lower().isalpha()))
    return {s[i:j] for i in range(300) for j in range(i + 50, i + 61) if s[i:j] == s[i:j][::-1] and s[i:j]}