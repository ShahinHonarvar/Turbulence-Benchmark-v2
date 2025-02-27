def palindromes_of_specific_lengths(s):
    s = s[21:95]
    palindromes = set()
    for length in range(52, 56):
        for start in range(len(s)):
            if s[start:start + length].lower() == s[start:start + length][::-1].lower():
                palindromes.add(s[start:start + length])
    return palindromes