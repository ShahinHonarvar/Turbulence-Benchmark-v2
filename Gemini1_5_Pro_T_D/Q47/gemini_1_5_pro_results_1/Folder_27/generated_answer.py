def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(13, 99 - 25):
        for length in range(26, 30):
            substring = s[i:i + length].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes