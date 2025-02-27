def palindromes_of_specific_lengths(s):
    s = s[11:92].lower()
    palindromes = set()
    for length in range(17, 67):
        for start in range(len(s) - length + 1):
            if all((c.isalpha() for c in s[start:start + length])) and s[start:start + length] == s[start:start + length][::-1]:
                palindromes.add(s[start:start + length])
    if palindromes:
        return palindromes
    else:
        return set()