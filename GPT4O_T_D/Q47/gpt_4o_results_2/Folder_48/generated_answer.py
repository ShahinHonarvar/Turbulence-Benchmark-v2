def palindromes_of_specific_lengths(s):
    s_filtered = ''.join(filter(str.isalpha, s[155:284].lower()))
    palindromes = set()
    n = len(s_filtered)
    for length in range(104, 121):
        for i in range(n - length + 1):
            substring = s_filtered[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes