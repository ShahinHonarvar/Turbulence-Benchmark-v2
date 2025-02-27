def palindromes_of_specific_lengths(s):
    s = s[17:73]
    cleaned_s = ''.join([c for c in s if c.isalpha()]).lower()
    palindromes = set()
    for length in range(50, 52):
        for i in range(len(cleaned_s) - length + 1):
            substring = cleaned_s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes