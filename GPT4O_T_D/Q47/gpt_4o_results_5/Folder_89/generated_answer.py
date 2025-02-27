def palindromes_of_specific_lengths(s):
    s = s[18:89]
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for length in range(12, 15):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes