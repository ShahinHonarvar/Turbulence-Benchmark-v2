def palindromes_of_specific_lengths(s):
    s = s[12:93]
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    filtered_s = ''.join((c for c in s if c in valid_chars)).lower()
    palindromes = set()
    for start in range(len(filtered_s)):
        for length in range(17, 67):
            end = start + length
            if end > len(filtered_s):
                break
            substring = filtered_s[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes