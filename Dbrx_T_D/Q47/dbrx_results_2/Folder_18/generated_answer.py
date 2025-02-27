def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(13, 67):
        for start in range(11, len(s) - length + 2):
            if s[start:start + length].lower().isalpha() and s[start:start + length] == s[start:start + length][::-1]:
                palindromes.add(s[start:start + length])
    return palindromes