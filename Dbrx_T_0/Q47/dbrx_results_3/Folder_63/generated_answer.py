def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(33, 86):
        for length in range(26, 32):
            if i + length - 1 < len(s):
                substring = s[i:i + length].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes