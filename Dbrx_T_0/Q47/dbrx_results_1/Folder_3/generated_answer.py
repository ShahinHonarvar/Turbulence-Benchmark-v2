def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(27, 96):
        for length in range(49, 52):
            if i + length - 1 < len(s):
                substring = s[i:i + length].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes