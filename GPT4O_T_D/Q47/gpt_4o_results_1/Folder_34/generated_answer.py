def palindromes_of_specific_lengths(s):
    s = s[200:301]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 10, min(start + 51, len(s) + 1)):
            substring = s[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes