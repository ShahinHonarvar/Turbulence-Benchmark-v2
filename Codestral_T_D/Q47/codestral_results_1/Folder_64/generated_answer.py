def palindromes_of_specific_lengths(s):
    s = s[:8]
    s = ''.join((ch.lower() for ch in s if ch.isalpha()))
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes