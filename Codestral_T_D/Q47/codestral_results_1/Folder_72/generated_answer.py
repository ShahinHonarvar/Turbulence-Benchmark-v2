def palindromes_of_specific_lengths(s):
    s = s[25:90]
    s = ''.join((ch for ch in s if ch.isalpha()))
    s = s.lower()
    palindromes = set()
    for length in range(27, 59):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes