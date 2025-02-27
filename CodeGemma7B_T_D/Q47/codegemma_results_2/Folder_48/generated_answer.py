def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for start in range(155, 283 + 1):
        for length in range(104, 120 + 1):
            end = start + length
            if s[start:end] == s[start:end][::-1]:
                palindromes.add(s[start:end])
    return palindromes