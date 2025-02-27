def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(130, 296):
        for length in range(103, 159):
            if i + length - 1 <= 295:
                substring = s[i:i + length].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes