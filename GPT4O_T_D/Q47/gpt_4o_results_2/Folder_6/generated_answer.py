def palindromes_of_specific_lengths(s):
    s = s[45:99]
    s = ''.join(filter(str.isalpha, s)).lower()
    valid_lengths = range(40, 48)
    palindromes = set()
    for length in valid_lengths:
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes