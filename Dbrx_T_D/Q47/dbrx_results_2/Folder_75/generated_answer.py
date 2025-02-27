def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(23, 40):
        for start in range(31, len(s) - length + 2):
            if s[start:start + length].lower() == s[start:start + length][::-1].lower():
                palindromes.add(s[start:start + length])
    return palindromes