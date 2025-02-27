def palindromes_of_specific_lengths(s):
    s = s[200:301]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for start in range(len(s)):
        for length in range(10, 51):
            end = start + length
            if end > len(s):
                break
            substring = s[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes