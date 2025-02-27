def palindromes_of_specific_lengths(s):
    s = s[15:96]
    clean_s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for start in range(len(clean_s)):
        for end in range(start + 20, min(start + 67, len(clean_s) + 1)):
            substring = clean_s[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes