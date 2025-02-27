def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(4, 6):
        for start in range(0, 8 - length + 1):
            substring = s[start:start + length].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes