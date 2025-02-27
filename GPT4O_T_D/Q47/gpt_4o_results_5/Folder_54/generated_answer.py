def palindromes_of_specific_lengths(s):
    s = s.lower()
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    if len(s) < 78:
        return palindromes
    for start in range(27, 78):
        for length in range(18, 20):
            end = start + length
            if end > 78:
                break
            substring = ''.join((c for c in s[start:end] if c in valid_chars))
            if len(substring) == length and substring == substring[::-1]:
                palindromes.add(s[start:end])
    return palindromes