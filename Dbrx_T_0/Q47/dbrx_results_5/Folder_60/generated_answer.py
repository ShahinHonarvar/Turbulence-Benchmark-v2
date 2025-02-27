def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(23, 83):
        for length in range(32, 35):
            if i + length <= 82:
                substring = s[i:i + length].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes