def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for start in range(15, 96):
        for length in range(20, 67):
            end = start + length
            if end > len(s):
                break
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes