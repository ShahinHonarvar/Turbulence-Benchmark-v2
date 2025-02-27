def palindromes_between_indices(s):
    s = ''.join((c.lower() for c in s[2:7] if c.isalpha()))
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 4, len(s) + 1) if s[i:j] == s[i:j][::-1]}
    return palindromes