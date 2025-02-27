def palindromes_of_specific_lengths(s):
    s = s[:101]
    palindromes = set()
    for length in range(3, 16):
        for i in range(0, 101 - length + 1):
            substring = s[i:i + length].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes